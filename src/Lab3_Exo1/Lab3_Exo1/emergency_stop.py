#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

def main():
    print("🚨 DÉMARRAGE ARRÊT D'URGENCE")
    
    # Initialise ROS2
    rclpy.init()
    
    # Crée un noeud
    node = Node('emergency_stop')
    
    # Crée le publisher
    publisher = node.create_publisher(String, 'emergency_stop', 10)
    
    # Donne du temps aux subscribers de se connecter
    print("Attente des abonnés...")
    time.sleep(2)  # Attente de 2 secondes
    
    # Crée le message
    msg = String()
    msg.data = 'STOP_ALL_ROBOTS_IMMEDIATELY'
    
    # Publie le message
    publisher.publish(msg)
    print("=" * 50)
    print("✅ ARRÊT D'URGENCE ACTIVÉ")
    print("Topic: /emergency_stop")
    print("Message: STOP_ALL_ROBOTS_IMMEDIATELY")
    print("=" * 50)
    
    # Donne du temps pour l'envoi
    time.sleep(0.5)
    
    # Nettoie
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()