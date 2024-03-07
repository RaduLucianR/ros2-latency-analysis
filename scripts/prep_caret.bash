#!/bin/bash

source /opt/ros/humble/setup.bash
source ~/ros2_caret_ws/install/local_setup.bash
source ~/ros_ws/install/local_setup.bash
export LD_PRELOAD=$(readlink -f ~/ros2_caret_ws/install/caret_trace/lib/libcaret.so)
