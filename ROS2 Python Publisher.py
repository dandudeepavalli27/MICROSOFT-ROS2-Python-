# SESSION 32 – ROS2 Python Publisher (15 Hz)

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PublisherNode(Node):

    def __init__(self):
        super().__init__('publisher_node')
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        
        # 15 Hz → 1/15 seconds
        timer_period = 1.0 / 15.0
        self.timer = self.create_timer(timer_period, self.publish_message)

    def publish_message(self):
        msg = String()
        msg.data = "Hello ROS2"
        self.publisher_.publish(msg)
        self.get_logger().info("Publishing at 15 Hz")

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
