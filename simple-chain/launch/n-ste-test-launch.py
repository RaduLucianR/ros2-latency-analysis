from launch import LaunchDescription
from launch_ros.actions import Node
from tracetools_launch.action import Trace
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    config_cores = os.path.join(
      get_package_share_directory('simple-chain'),
      'config',
      'exec-cpu-n-per-1-node.yaml'
      )
    
    config_payload = os.path.join(
      get_package_share_directory('simple-chain'),
      'config',
      'msg_sizes.yaml'
      )
    
    return LaunchDescription([
        # Trace(
        #     session_name='e2e_sample_launch',
        #     events_kernel=[],
        #     events_ust=['ros2*']
        # ),

        Node(
            package='simple-chain',
            executable='n-ste',
            arguments=[config_cores],
            parameters=[config_payload]
        ),
    ])
