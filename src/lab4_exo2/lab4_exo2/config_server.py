#!/usr/bin/env python3
# type: ignore

import rclpy
from rclpy.node import Node
from lab4_exo2.srv import ConfigureRobot

class ConfigServer(Node):
    def __init__(self):
        super().__init__('config_server')
        self.service = self.create_service(
            ConfigureRobot,
            'configure_robot',
            self.callback
        )
        print('Serveur pret!')
    
    def callback(self, request, response):
        print(f'Robot: {request.robot_id}')
        response.success = True
        response.message = 'OK'
        response.configuration_id = 'CONFIG_001'
        return response

def main():
    rclpy.init()
    server = ConfigServer()
    rclpy.spin(server)

if __name__ == '__main__':
    main()