import os
import launch
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch.actions import ExecuteProcess
from launch_ros.actions import Node


def generate_launch_description():
    os.environ["IGN_GAZEBO_RESOURCE_PATH"] = os.path.join(
        FindPackageShare('camera-sensor-example').find("camera-sensor-example"), 'models')

    gazebo = ExecuteProcess(
        cmd=[[
            'ign gazebo ',
            PathJoinSubstitution([
                FindPackageShare('camera-sensor-example'),
                'worlds',
                'arashs_wonderland.sdf '
            ]),
            '--render-engine ogre ',
            '-v 4 '
        ]],
        shell=True
    )
    rviz = Node(
        package='rviz2',
        executable='rviz2',
    )
    bridge = Node(
        package='ros_ign_bridge',
        executable='parameter_bridge',
        arguments=['/camera@sensor_msgs/msg/Image@ignition.msgs.Image'],
    )
    return launch.LaunchDescription([
        gazebo,
        bridge,
        rviz
    ])
