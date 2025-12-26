#!/usr/bin/env python3
# type: ignore  # Désactive les vérifications pour éviter le rouge

import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter

class PIDController(Node):
    def __init__(self):
        super().__init__('pid_controller')
        
        # Déclare les paramètres avec valeurs par défaut
        self.declare_parameters(
            namespace='',
            parameters=[
                ('kp', 1.0),           # Gain proportionnel
                ('ki', 0.1),           # Gain intégral
                ('kd', 0.05),          # Gain dérivé
                ('max_output', 100.0), # Sortie maximale
                ('min_output', -100.0),# Sortie minimale
                ('integral_limit', 50.0), # Limite anti-windup
                ('config_name', 'default') # Nom de la config
            ]
        )
        
        # Récupère les paramètres
        self.kp = self.get_parameter('kp').value
        self.ki = self.get_parameter('ki').value
        self.kd = self.get_parameter('kd').value
        self.max_output = self.get_parameter('max_output').value
        self.min_output = self.get_parameter('min_output').value
        self.integral_limit = self.get_parameter('integral_limit').value
        self.config_name = self.get_parameter('config_name').value
        
        # Valide les paramètres
        self.validate_parameters()
        
        # Affiche la configuration
        self.print_configuration()
        
        # S'abonne aux changements de paramètres
        self.add_on_set_parameters_callback(self.parameters_callback)
        
        self.get_logger().info('✅ Contrôleur PID initialisé!')
    
    def validate_parameters(self):
        """Valide les paramètres PID"""
        # Gains doivent être non-négatifs
        if self.kp < 0 or self.ki < 0 or self.kd < 0:
            self.get_logger().error('❌ Erreur: Les gains (kp, ki, kd) doivent être >= 0')
            raise ValueError("Gains PID négatifs")
        
        # max_output > min_output
        if self.max_output <= self.min_output:
            self.get_logger().error('❌ Erreur: max_output doit être > min_output')
            raise ValueError("max_output <= min_output")
        
        # integral_limit > 0
        if self.integral_limit <= 0:
            self.get_logger().error('❌ Erreur: integral_limit doit être > 0')
            raise ValueError("integral_limit <= 0")
        
        self.get_logger().info('✅ Paramètres validés avec succès')
    
    def print_configuration(self):
        """Affiche la configuration courante"""
        self.get_logger().info('=' * 50)
        self.get_logger().info(f'📋 CONFIGURATION PID: {self.config_name}')
        self.get_logger().info(f'  kp: {self.kp}')
        self.get_logger().info(f'  ki: {self.ki}')
        self.get_logger().info(f'  kd: {self.kd}')
        self.get_logger().info(f'  Sortie max/min: {self.max_output}/{self.min_output}')
        self.get_logger().info(f'  Limite intégrale: {self.integral_limit}')
        self.get_logger().info('=' * 50)
    
    def parameters_callback(self, params):
        """Callback appelé quand les paramètres changent"""
        successful = []
        failed = []
        
        for param in params:
            # Met à jour les attributs
            if param.name == 'kp':
                if param.value >= 0:
                    self.kp = param.value
                    successful.append(f'kp={param.value}')
                else:
                    failed.append(f'kp ({param.value}) doit être >= 0')
            
            elif param.name == 'ki':
                if param.value >= 0:
                    self.ki = param.value
                    successful.append(f'ki={param.value}')
                else:
                    failed.append(f'ki ({param.value}) doit être >= 0')
            
            elif param.name == 'kd':
                if param.value >= 0:
                    self.kd = param.value
                    successful.append(f'kd={param.value}')
                else:
                    failed.append(f'kd ({param.value}) doit être >= 0')
            
            elif param.name == 'max_output':
                if param.value > self.min_output:
                    self.max_output = param.value
                    successful.append(f'max_output={param.value}')
                else:
                    failed.append(f'max_output ({param.value}) doit être > min_output ({self.min_output})')
            
            elif param.name == 'min_output':
                if param.value < self.max_output:
                    self.min_output = param.value
                    successful.append(f'min_output={param.value}')
                else:
                    failed.append(f'min_output ({param.value}) doit être < max_output ({self.max_output})')
            
            elif param.name == 'integral_limit':
                if param.value > 0:
                    self.integral_limit = param.value
                    successful.append(f'integral_limit={param.value}')
                else:
                    failed.append(f'integral_limit ({param.value}) doit être > 0')
            
            elif param.name == 'config_name':
                self.config_name = param.value
                successful.append(f'config_name={param.value}')
        
        # Log les résultats
        if successful:
            self.get_logger().info(f'✅ Paramètres mis à jour: {", ".join(successful)}')
            self.print_configuration()
        
        if failed:
            for fail in failed:
                self.get_logger().error(f'❌ {fail}')
        
        # Retourne le résultat
        result = rclpy.node.SetParametersResult()
        result.successful = len(failed) == 0
        return result
    
    def compute_pid(self, error, dt=0.01):
        """Calcule la sortie PID (méthode exemple)"""
        # Variables pour l'intégrale et la dérivée
        if not hasattr(self, 'integral'):
            self.integral = 0.0
            self.previous_error = error
        
        # Calcul PID
        self.integral += error * dt
        derivative = (error - self.previous_error) / dt
        
        # Anti-windup
        if abs(self.integral) > self.integral_limit:
            self.integral = self.integral_limit if self.integral > 0 else -self.integral_limit
        
        # Sortie PID
        output = (self.kp * error + 
                 self.ki * self.integral + 
                 self.kd * derivative)
        
        # Limitation de sortie
        output = max(self.min_output, min(self.max_output, output))
        
        self.previous_error = error
        return output

def main(args=None):
    rclpy.init(args=args)
    
    try:
        # Crée et exécute le contrôleur PID
        pid_controller = PIDController()
        rclpy.spin(pid_controller)
    except ValueError as e:
        print(f"❌ Erreur d'initialisation: {e}")
    except KeyboardInterrupt:
        print("\n👋 Arrêt du contrôleur PID")
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()