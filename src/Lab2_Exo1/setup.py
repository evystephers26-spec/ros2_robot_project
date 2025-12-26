from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'Lab2_Exo1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # CETTE LIGNE EST ESSENTIELLE pour inclure les services
        (os.path.join('share', package_name, 'srv'), glob('srv/*.srv')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='assimarcaurele',
    maintainer_email='assimarcaurele@example.com',
    description='Calculator Service - Lab2 Exercise 1',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'calculator_server = Lab2_Exo1.calculator_server:main',
            'calculator_client = Lab2_Exo1.calculator_client:main',
        ],
    },
)