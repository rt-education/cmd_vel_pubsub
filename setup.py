from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'cmd_vel_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='RT Corporation',
    maintainer_email='edu@rt-net.jp',
    description='',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = cmd_vel_pubsub.publisher_member_function:main',
            'listener = cmd_vel_pubsub.subscriber_member_function:main',
            'cmd_vel_talker = cmd_vel_pubsub.cmd_vel_publisher:main',
        ],
    },
)
