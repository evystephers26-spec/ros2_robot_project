from setuptools import find_packages, setup

package_name = 'warehouse_robot'

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
    maintainer='assimarcaurele',
    maintainer_email='assimarcaurele@example.com',
    description='Warehouse robot with BT strategies',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
            entry_points={
        'console_scripts': [
            'robot_controller = warehouse_robot.robot_strategies:main',
        ],
    

    },
)
