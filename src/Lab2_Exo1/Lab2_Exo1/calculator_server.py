#!/usr/bin/env python3
# type: ignore
import rclpy
from rclpy.node import Node
from Lab2_Exo1.srv import Calculator

class CalculatorServer(Node):
    def __init__(self):
        super().__init__('calculator_server')
        self.service = self.create_service(Calculator, 'calculate', self.calculate_callback)
        self.get_logger().info('Serveur pret!')
    
    def calculate_callback(self, request, response):
        a = request.a
        b = request.b
        operation = request.operation
        
        if operation == "add":
            response.result = a + b
            response.success = True
            response.message = "Addition reussie"
        elif operation == "subtract":
            response.result = a - b
            response.success = True
            response.message = "Soustraction reussie"
        elif operation == "multiply":
            response.result = a * b
            response.success = True
            response.message = "Multiplication reussie"
        elif operation == "divide":
            if b != 0:
                response.result = a / b
                response.success = True
                response.message = "Division reussie"
            else:
                response.result = 0
                response.success = False
                response.message = "Erreur: Division par zero!"
        else:
            response.result = 0
            response.success = False
            response.message = f"Operation inconnue: {operation}"
        
        return response

def main(args=None):
    rclpy.init(args=args)
    server = CalculatorServer()
    try:
        rclpy.spin(server)
    except KeyboardInterrupt:
        pass
    finally:
        server.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()