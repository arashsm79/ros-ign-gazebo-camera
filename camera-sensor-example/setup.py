import os
from glob import glob
from setuptools import setup

package_name = 'camera-sensor-example'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, "worlds"), glob('worlds/*.sdf')),
        (os.path.join('share', package_name, "models", "arashcamera"),
         glob('models/arashcamera/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='arashsm79',
    maintainer_email='arashsm79@yahoo.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
