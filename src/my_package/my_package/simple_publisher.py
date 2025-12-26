#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):
    def __init__(self):
        super().__init__('simple_publisher')
        
        # Crée un publisher pour le topic "chatter"
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        
        # Timer à 0.5 secondes (2 fois par seconde)
        timer_period = 0.5  # secondes
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        self.i = 0
    
    def timer_callback(self):
        # Crée le message
        msg = String()
        
        # ICI : METS TON PRÉNOM !
        msg.data = 'Mathis'  # Remplace 'Mathis' par TON prénom
        
        # Publie le message
        self.publisher_.publish(msg)
        
        # Affiche dans le terminal
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

def main(args=None):
    # Initialise ROS2
    rclpy.init(args=args)
    
    # Crée le publisher
    simple_publisher = SimplePublisher()
    
    # Lance le programme
    try:
        rclpy.spin(simple_publisher)
    except KeyboardInterrupt:
        pass
    finally:
        # Nettoie avant de quitter
        simple_publisher.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()