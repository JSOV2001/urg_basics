#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class ScanSubscriber(Node):
    def __init__(self):
        super().__init__("scan_subscriber")
        scan_sub = self.create_subscription(LaserScan, "/scan", self.scan_callback, 10)
    
    def scan_callback(self, scan_msg):
        print(f"\nScan's TIme: {scan_msg.scan_time} s")

def main():
    rclpy.init()
    try:
        node = ScanSubscriber()
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()