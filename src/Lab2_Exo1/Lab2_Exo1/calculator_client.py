#!/usr/bin/env python3
# type: ignore
import sys
import rclpy
from rclpy.node import Node
from Lab2_Exo1.srv import Calculator

class CalculatorClient(Node):
    def __init__(self):
        super().__init__('calculator_client')
        self.client = self.create_client(Calculator, 'calculate')
        
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Attente...')
        
        self.get_logger().info('Connecte!')
    
    def send_request(self, a, b, operation):
        request = Calculator.Request()
        request.a = float(a)
        request.b = float(b)
        request.operation = operation
        
        self.get_logger().info(f'Envoi: {a} {operation} {b}')
        
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        
        if future.result() is not None:
            response = future.result()
            if response.success:
                print(f'SUCCES: {response.message}')
                print(f'RESULTAT: {response.result}')
            else:
                print(f'ERREUR: {response.message}')
        else:
            print('ERREUR: Pas de reponse')

def main(args=None):
    rclpy.init(args=args)
    
    if len(sys.argv) != 4:
        print("Usage: ros2 run Lab2_Exo1 calculator_client <nb1> <nb2> <operation>")
        print("Operations: add, subtract, multiply, divide")
        return
    
    client = CalculatorClient()
    
    try:
        a = sys.argv[1]
        b = sys.argv[2]
        operation = sys.argv[3]
        
        client.send_request(a, b, operation)
        
    except ValueError:
        print("ERREUR: Nombres invalides")
    except Exception as e:
        print(f"ERREUR: {e}")
    finally:
        client.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()