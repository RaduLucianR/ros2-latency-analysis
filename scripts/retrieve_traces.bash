#!/bin/bash

# Default values for optional parameters
default_source_folder="/home/pi/.ros/tracing"
default_destination_folder="/home/${USER}/tracing"
default_user="pi"
default_password="raspberry"
all_folders=false

# Function to display usage
usage() {
    echo "Retrieve trace folder from a Raspberry Pi and create CARET architecture file"
    echo "Usage: $0 -i <IP address> [-s <source folder>] [-d <destination folder>]"
    echo "  -i IP address (mandatory): string with format xxx.xxx.xxx.xxx"
    echo "  -s source folder (optional): path as string, default is $default_source_folder"
    echo "  -d destination folder (optional): path as string, default is $default_destination_folder"
    echo "  -u user for the Raspberry Pi (optional), default is $default_user"
    echo "  -p password for the Raspberry Pi (optional), default is $default_password"
    echo "  -a process all trace folders (optional)"
    exit 1
}

# Check if at least one argument is provided
if [ $# -eq 0 ]; then
    usage
fi

# Parse the command-line arguments
while getopts ":i:s:d:u:p:a" opt; do
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
    a)
      all_folders=true
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

# Source ROS2 and CARET
source /opt/ros/humble/setup.bash
source ~/ros2_caret_ws/install/local_setup.bash

if [ "$all_folders" = true ]; then
  archive_name="traces_$(date +%Y%m%d_%H%M%S).tar.gz"
  sshpass -p "${password}" ssh "${user}"@"${IP}" "tar -czvf ${source_folder}/${archive_name} -C ${source_folder} ."
  sshpass -p "${password}" scp "${user}"@"${IP}":"${source_folder}/${archive_name}" ${destination_folder}
  sshpass -p "${password}" ssh "${user}"@"${IP}" "rm -rf ${source_folder}/${archive_name}"
  tar -xzvf ${destination_folder}/${archive_name} -C ${destination_folder}
  rm -rf ${destination_folder}/${archive_name}

  for subdir in "$destination_folder"/*; do
    # Check if the item is a directory
    if [ -d "$subdir" ]; then
        echo "Processing trace folder: $subdir"
        subdir_f="${subdir##*/}"
        ros2 caret create_architecture_file ${subdir} -o ${destination_folder}/archi-${subdir_f}.yaml
    fi
  done
else
  # Retrieve the latest created sub-folder
  latest_created_folder=$(sshpass -p "${password}" ssh "${user}"@"${IP}" "ls -lt ${source_folder} | grep ^d | head -n 1 | awk '{print \$9}'")
  folder_name=$latest_created_folder
  sshpass -p "${password}" ssh "${user}"@"${IP}" "tar -czvf ${source_folder}/${folder_name}.tar.gz -C ${source_folder} ${folder_name}"
  sshpass -p "${password}" scp "${user}"@"${IP}":"${source_folder}/${folder_name}.tar.gz" ${destination_folder}
  sshpass -p "${password}" ssh "${user}"@"${IP}" "rm -rf ${source_folder}/${folder_name}.tar.gz"
  tar -xzvf ${destination_folder}/${folder_name}.tar.gz -C ${destination_folder}
  rm -rf ${destination_folder}/${folder_name}.tar.gz
  ros2 caret create_architecture_file ${destination_folder}/${folder_name} -o ${destination_folder}/archi-${folder_name}.yaml
fi