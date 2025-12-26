from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'lab4_exo2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # IMPORTANT: inclure les fichiers .srv
        (os.path.join('share', package_name, 'srv'), glob('srv/*.srv')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='assimarcaurele',
    maintainer_email='assimarcaurele@example.com',
    description='Robot Configuration Service',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'config_server = lab4_exo2.config_server:main',
            'config_client = lab4_exo2.config_client:main',
        ],
    },
)
