import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'multi_sensor_dashboard'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='asus',
    maintainer_email='spurthiraj292006@gmail.com',
    description='Multi-sensor dashboard ROS 2 project',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ultrasonic_publisher = multi_sensor_dashboard.ultrasonic_publisher:main',
            'imu_publisher = multi_sensor_dashboard.imu_publisher:main',
            'battery_publisher = multi_sensor_dashboard.battery_publisher:main',
            'dashboard_aggregator = multi_sensor_dashboard.dashboard_aggregator:main',
        ],
    },
)
