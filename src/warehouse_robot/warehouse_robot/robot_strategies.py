#!/usr/bin/env python3
# type: ignore

import rclpy
from rclpy.node import Node

class WarehouseRobot(Node):
    def __init__(self):
        super().__init__('warehouse_robot')
        
        print("=" * 60)
        print("🤖 ROBOT D'ENTREPÔT - STRATÉGIES BEHAVIOR TREE")
        print("=" * 60)
        
        # Affiche les réponses aux questions
        self.explain_strategies()
        
        print("=" * 60)
        print("✅ SCÉNARIO COMPRIS ET RÉSOLU")
        print("=" * 60)
    
    def explain_strategies(self):
        """Explique les stratégies pour chaque tâche"""
        
        print("\n📦 1. LIVRAISON DE COLIS (20-30 min)")
        print("   Stratégie: NODE SÉQUENCE (Sequence Node)")
        print("   Pourquoi: Les étapes doivent être dans l'ordre:")
        print("     1. Aller chercher le colis")
        print("     2. Porter le colis")
        print("     3. Naviguer vers destination")
        print("     4. Déposer le colis")
        print("     5. Retourner à la base")
        print("   → Comme une recette de cuisine, étape par étape!")
        
        print("\n🔋 2. URGENCE BATTERIE FAIBLE")
        print("   Stratégie: NODE DE RÉCUPÉRATION (Recovery Node)")
        print("   Pourquoi: Priorité ABSOLUE - sécurité du robot:")
        print("     1. Arrêter immédiatement la tâche en cours")
        print("     2. Naviguer vers station de charge")
        print("     3. Attendre recharge complète")
        print("     4. Reprendre les opérations")
        print("   → Comme quand ton portable dit '1%' - tu branches!")
        
        print("\n⏰ 3. RECHARGE PROGRAMMÉE")
        print("   Stratégie: NODE PARALLÈLE (Parallel Node)")
        print("   Pourquoi: Le robot peut faire plusieurs choses:")
        print("     - Continuer sa livraison en cours")
        print("     - Se diriger vers la station")
        print("     - Arrêter seulement à l'arrivée")
        print("   → Comme marcher en mâchant du chewing-gum!")
        
        print("\n🎯 4. MULTIPLES STRATÉGIES SUR LE MÊME ROBOT?")
        print("   Réponse: OUI, ABSOLUMENT!")
        print("   Pourquoi: Un robot intelligent adapte sa stratégie:")
        print("     - Mode normal: SÉQUENCE (livraison)")
        print("     - Mode urgence: RÉCUPÉRATION (batterie)")
        print("     - Mode maintenance: PARALLÈLE (recharge)")
        print("   → Comme toi: étudier, manger, dormir - différentes stratégies!")

def main(args=None):
    rclpy.init(args=args)
    
    robot = WarehouseRobot()
    
    # Garde le node actif pour pouvoir lire
    print("\nAppuyez sur Ctrl+C pour quitter...")
    try:
        rclpy.spin(robot)
    except KeyboardInterrupt:
        print("\n👋 Fermeture du robot d'entrepôt")
    finally:
        robot.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()