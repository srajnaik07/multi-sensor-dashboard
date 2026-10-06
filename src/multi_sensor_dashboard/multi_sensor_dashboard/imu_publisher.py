import rclpy
from rclpy.node import Node
from multi_sensor_interfaces.msg import SensorStatus
import random


class ImuPublisher(Node):

    def __init__(self):
        super().__init__('imu_publisher')

        self.publisher_ = self.create_publisher(
            SensorStatus,
            '/imu',
            10
        )

        self.timer = self.create_timer(
            0.5,
            self.publish_orientation
        )

    def publish_orientation(self):
        msg = SensorStatus()

        msg.roll = random.uniform(-180.0, 180.0)
        msg.pitch = random.uniform(-90.0, 90.0)
        msg.yaw = random.uniform(-180.0, 180.0)

        self.publisher_.publish(msg)

        self.get_logger().info(
            f'Roll: {msg.roll:.2f}°, '
            f'Pitch: {msg.pitch:.2f}°, '
            f'Yaw: {msg.yaw:.2f}°'
        )


def main(args=None):
    rclpy.init(args=args)

    node = ImuPublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
