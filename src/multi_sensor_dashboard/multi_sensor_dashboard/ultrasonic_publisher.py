import random

import rclpy
from rclpy.node import Node
from multi_sensor_interfaces.msg import SensorStatus


class UltrasonicPublisher(Node):

    def __init__(self):
        super().__init__('ultrasonic_publisher')

        self.publisher_ = self.create_publisher(
            SensorStatus,
            '/ultrasonic',
            10
        )

        self.timer = self.create_timer(
            0.5,
            self.publish_distance
        )

    def publish_distance(self):
        msg = SensorStatus()
        msg.distance = random.uniform(1.0, 10.0)

        self.publisher_.publish(msg)

        self.get_logger().info(
            f'Distance: {msg.distance:.2f} m'
        )


def main(args=None):
    rclpy.init(args=args)

    node = UltrasonicPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
