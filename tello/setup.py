from setuptools import setup
import os
from glob import glob

setup(
    name='tello',
    version='0.1.0',
    packages=['tello'],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/tello']),
        ('share/tello', ['package.xml', 'resource/ost.txt', 'resource/ost.yaml']),
        (os.path.join("share", "tello", "launch"), glob(os.path.join("launch", "*.launch.py"))),
        (os.path.join("share", "tello", "config"), glob(os.path.join("config", "*")))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tentone',
    maintainer_email='tentone@outlook.com',
    description='DJI Tello control package for ROS 2',
    license='MIT',
    tests_require=[],
    entry_points={
        'console_scripts': [
            'tello = tello.node:main'
        ],
    },
)
