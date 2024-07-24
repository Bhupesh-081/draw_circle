import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircleNode(Node):
    def __init__(self):
        super().__init__('draw_circle')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        timer_period = 0.1 
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Draw Circle Node has been started.')

    def timer_callback(self):
        vel_msg = Twist()
        vel_msg.linear.x = 2.0  
        vel_msg.angular.z = 1.0 
        self.publisher_.publish(vel_msg)

def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.spin(node)
    rclpy.shutdown()

