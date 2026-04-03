# MICROSOFT-ROS2-Python
Aim
To implement a ROS2 Python node that publishes messages at a fixed rate.
General Objective
To develop proficiency in programming ROS2 nodes using Python and evaluate real-time communication performance.
Specific Objective
To publish messages at:
15 Hz (15 messages per second)
If system maintains rate → Real-Time Performance Achieved
Dataset
ROS2 rclpy Examples
Source: ROS2 Examples Repository
Procedure
Import ROS2 libraries
Create publisher node
Set timer for 15 Hz
Publish messages continuously
Verify publishing rate
Display result
Algorithm
Start
Initialize ROS2 node
Set publishing frequency (15 Hz)
Publish messages
Monitor execution
Display result
Stop
Code Logic
timer_period = 1 / 15
Python Code
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
Output
Publishing at 15 Hz
Publishing at 15 Hz
...
Real-Time Performance Achieved
Result
The ROS2 node successfully publishes messages at:
15 Hz
Real-Time Performance Achieved
Industry Application
ROS2 communication is used in:
Robotics systems
Autonomous vehicles
Industrial automation
Real-time AI systems
Companies like Microsoft use such systems in:
Cloud robotics
AI-based automation
Real-time distributed systems
Conclusion
ROS2 enables efficient real-time communication, making it ideal for modern autonomous robotic applications.
