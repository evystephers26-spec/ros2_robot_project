#!/usr/bin/env python3
# type: ignore

import sys
import rclpy
from rclpy.node import Node
from lab4_exo2.srv import ConfigureRobot

class ConfigClient(Node):
    def __init__(self):
        super().__init__('config_client')
        self.client = self.create_client(ConfigureRobot, 'configure_robot')
        while not self.client.wait_for_service(timeout_sec=1.0):
            print('Attente service...')
        print('Service trouve!')
    
    def send(self, robot_id, max_vel, accel, safety, collision, auto_charge):
        req = ConfigureRobot.Request()
        req.robot_id = robot_id
        req.max_velocity = float(max_vel)
        req.acceleration_limit = float(accel)
        req.safety_distance = float(safety)
        req.enable_collision_avoidance = collision == 'true'
        req.enable_auto_charging = auto_charge == 'true'
        
        future = self.client.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        
        if future.result():
            print('Reponse:', future.result().message)

def main():
    if len(sys.argv) != 7:
        print('Usage: ros2 run lab4_exo2 config_client robot_id max_vel accel safety collision auto_charge')
        return
    
    rclpy.init()
    client = ConfigClient()
    client.send(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])

if __name__ == '__main__':
    main()