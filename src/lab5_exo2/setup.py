from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'lab5_exo2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Inclut les fichiers YAML de configuration
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='assimarcaurele',
    maintainer_email='assimarcaurele@example.com',
    description='PID Controller with parameters - Lab5 Exercise 2',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pid_controller = lab5_exo2.pid_controller:main',
        ],
    },
)