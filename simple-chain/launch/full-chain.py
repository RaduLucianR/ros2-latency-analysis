from launch import LaunchDescription
from launch_ros.actions import Node
from tracetools_launch.action import Trace

def generate_launch_description():
    return LaunchDescription([
        Trace(
            session_name='e2e_sample_launch',
            events_kernel=[],
            events_ust=['ros2*']
        ),

        Node(
            package='simple-chain',
            executable='camera',
        ),

        Node(
            package='simple-chain',
            executable='fusion',
        ),

        Node(
            package='simple-chain',
            executable='perception',
        ),

        Node(
            package='simple-chain',
            executable='planning',
        ),

        Node(
            package='simple-chain',
            executable='control',
        ),

        Node(
            package='simple-chain',
            executable='actuator',
        ),

    ])
