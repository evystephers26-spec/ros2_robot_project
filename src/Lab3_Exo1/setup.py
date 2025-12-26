from setuptools import find_packages, setup

package_name = 'Lab3_Exo1'

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
    description='Emergency Stop for Robot Fleet',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
        entry_points={
        'console_scripts': [
            'emergency_stop = Lab3_Exo1.emergency_stop:main',
            'test_emergency = Lab3_Exo1.test_emergency:main',
        ],
    },
    
)
