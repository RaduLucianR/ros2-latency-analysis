#!/bin/bash

# Default values for optional parameters
default_source_folder="/home/pi/.ros/tracing"
default_destination_folder="/home/${USER}/tracing"
default_user="pi"
default_password="raspberry"

# Function to display usage
usage() {
    echo "Retrieve trace folder from a Raspberry Pi and create CARET architecture file"
    echo "Usage: $0 -i <IP address> [-s <source folder>] [-d <destination folder>]"
    echo "  -i IP address (mandatory): string with format xxx.xxx.xxx.xxx"
    echo "  -s source folder (optional): path as string, default is $default_source_folder"
    echo "  -d destination folder (optional): path as string, default is $default_destination_folder"
    echo "  -u user for the Raspberry Pi (optional), default is $default_user"
    echo "  -p password for the Raspberry Pi (optional), default is $default_password"
    exit 1
}

# Check if at least one argument is provided
if [ $# -eq 0 ]; then
    usage
fi

# Parse the command-line arguments
while getopts ":i:s:d:u:p:" opt; do
  case $opt in
    i)
      IP=$OPTARG
      ;;
    s)
      source_folder=$OPTARG
      ;;
    d)
      destination_folder=$OPTARG
      ;;
    u)
      user=$OPTARG
      ;;
    p)
      password=$OPTARG
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      usage
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      usage
      ;;
  esac
done

# Validate the IP address format
if ! [[ $IP =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    echo "Error: IP address must be in the format xxx.xxx.xxx.xxx"
    exit 1
fi

# Set parameters to default values if other not provided
source_folder=${source_folder:-$default_source_folder}
destination_folder=${destination_folder:-$default_destination_folder}
user=${user:-$default_user}
password=${password:-$default_password}

# Find the latest created sub-folder under the source_folder
latest_created_folder=$(sshpass -p "${password}" ssh "${user}"@"${IP}" "ls -lt ${source_folder} | grep ^d | head -n 1 | awk '{print \$9}'")

# gzip the latest_created_folder
sshpass -p "${password}" ssh "${user}"@"${IP}" "tar -czvf ${source_folder}/${latest_created_folder}.tar.gz -C ${source_folder} ${latest_created_folder}"

# Copy the gzip locally
sshpass -p "${password}" scp "${user}"@"${IP}":"${source_folder}/${latest_created_folder}.tar.gz" ${destination_folder}

# Remove the gzip remotely
sshpass -p "${password}" ssh "${user}"@"${IP}" "rm -rf ${source_folder}/${latest_created_folder}.tar.gz"

# Unzip the gzip
tar -xzvf ${destination_folder}/${latest_created_folder}.tar.gz -C ${destination_folder}

# Remove gzip
rm -rf ${destination_folder}/${latest_created_folder}.tar.gz

# Source ROS2 and CARET
source /opt/ros/humble/setup.bash
source ~/ros2_caret_ws/install/local_setup.bash

# Create CARET architecture file from traces
ros2 caret create_architecture_file ${destination_folder}/${latest_created_folder} -o ${destination_folder}/archi-${latest_created_folder}.yaml