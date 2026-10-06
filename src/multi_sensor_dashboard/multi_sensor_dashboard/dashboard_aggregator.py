import rclpy
from rclpy.node import Node
from multi_sensor_interfaces.msg import SensorStatus


class DashboardAggregator(Node):

    def __init__(self):
        super().__init__('dashboard_aggregator')

        self.distance = None
        self.roll = None
        self.pitch = None
        self.yaw = None
        self.battery = None

        self.ultrasonic_subscription = self.create_subscription(
            SensorStatus,
            '/ultrasonic',
            self.ultrasonic_callback,
            10
        )

        self.imu_subscription = self.create_subscription(
            SensorStatus,
            '/imu',
            self.imu_callback,
            10
        )

        self.battery_subscription = self.create_subscription(
            SensorStatus,
            '/battery',
            self.battery_callback,
            10
        )

    def ultrasonic_callback(self, msg):
        self.distance = msg.distance
        self.print_dashboard()

    def imu_callback(self, msg):
        self.roll = msg.roll
        self.pitch = msg.pitch
        self.yaw = msg.yaw
        self.print_dashboard()

    def battery_callback(self, msg):
        self.battery = msg.battery
        self.print_dashboard()

    def print_dashboard(self):

        if (
            self.distance is not None
            and self.roll is not None
            and self.pitch is not None
            and self.yaw is not None
            and self.battery is not None
        ):
            self.get_logger().info(
                f'DASHBOARD | '
                f'Distance: {self.distance:.2f} m | '
                f'Roll: {self.roll:.2f}° | '
                f'Pitch: {self.pitch:.2f}° | '
                f'Yaw: {self.yaw:.2f}° | '
                f'Battery: {self.battery}%'
            )


def main(args=None):
    rclpy.init(args=args)

    node = DashboardAggregator()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()	
