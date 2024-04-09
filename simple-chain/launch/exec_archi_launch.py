from launch import LaunchDescription
from launch.actions import TimerAction, Shutdown, DeclareLaunchArgument
from launch_ros.actions import Node
from tracetools_launch.action import Trace
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import os
import time

def generate_launch_description():
    configs = os.path.join(
      get_package_share_directory('simple-chain'),
      'config',
      'executor_architecture_template.yaml'
      )
    
    return LaunchDescription([
        DeclareLaunchArgument(
            'trfolder',  # Name of the argument
            default_value=time.strftime(f"e2e_%Y%m%d-%H%M%S"),  # Default value
            description='Trace folder name'
        ),

        Trace(
            session_name=LaunchConfiguration('trfolder'),
            events_kernel=[],
            events_ust=['ros2*']
        ),

        Node(
            package='simple-chain',
            executable='exec_archi',
            arguments=[configs]
        ),

        TimerAction(
            period=120.0,  # time in seconds after which the shutdown will be triggered
            actions=[
                Shutdown(reason='Time limit reached')
            ]
        )
    ])
