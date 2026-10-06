import rclpy
from rclpy.node import Node
from multi_sensor_interfaces.msg import SensorStatus
import random


class BatteryPublisher(Node):

    def __init__(self):
        super().__init__('battery_publisher')

        self.publisher_ = self.create_publisher(
            SensorStatus,
            '/battery',
            10
        )

        self.timer = self.create_timer(
            0.5,
            self.publish_battery
        )

    def publish_battery(self):
        msg = SensorStatus()

        msg.battery = random.randint(0, 100)

        self.publisher_.publish(msg)

        self.get_logger().info(
            f'Battery: {msg.battery}%'
        )


def main(args=None):
    rclpy.init(args=args)

    node = BatteryPublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
