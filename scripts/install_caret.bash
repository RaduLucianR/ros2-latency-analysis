#!/bin/bash

if ! command -v ros2 &> /dev/null
then
    echo "ROS2 is not installed. Why do you even want to install CARET??"
fi

if ! command -v colcon &> /dev/null
then
    echo "Colcon is not installed. Install colcon first!"
fi

cd # Install in under home directory
git clone https://github.com/tier4/caret.git ros2_caret_ws
cd ros2_caret_ws
mkdir src

if ! command -v vcs &> /dev/null
then
    echo "vcs could not be found"
    echo "Installing vcs..."

    sudo apt install python3-vcstool
fi

vcs import src < caret.repos
echo "Running setup_caret..."
./setup_caret.sh
source /opt/ros/humble/setup.bash
colcon build --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release
source ~/ros2_caret_ws/install/local_setup.bash
ros2 run tracetools status # return Tracing enabled
echo "If you see Tracing enabled then installation successful!"
