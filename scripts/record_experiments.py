import subprocess
import yaml

def update_payload(file_path, new_size):
    # Load the YAML file
    with open(file_path, 'r') as stream:
        data = yaml.safe_load(stream)

    # Update the message_size for each specified key
    keys_to_update = ['/talker']
    for key in keys_to_update:
        if key in data and 'ros__parameters' in data[key]:
            data[key]['ros__parameters']['message_size'] = new_size

    # Overwrite the YAML file with the new data
    with open(file_path, 'w') as stream:
        yaml.dump(data, stream, default_flow_style=False)

def update_cores(file_path, core_values):
    # Load the YAML file
    with open(file_path, 'r') as stream:
        data = yaml.safe_load(stream)

    # Update the core values for each specified thread
    for thread, core in core_values.items():
        if thread in data:
            data[thread]['core'] = core

    # Overwrite the YAML file with the new data
    with open(file_path, 'w') as stream:
        yaml.dump(data, stream, default_flow_style=False)

def cores_string(core_values):
    concatenated_values = ""

    for value in core_values.values():
        concatenated_values += str(value)

    return concatenated_values

def run_experiment(executors, name):
    commands = f"""
    source /opt/ros/humble/setup.bash
    source ~/ros2_caret_ws/install/local_setup.bash
    source ~/ros_ws/install/local_setup.bash
    export LD_PRELOAD=$(readlink -f ~/ros2_caret_ws/install/caret_trace/lib/libcaret.so)
    ros2 launch simple-chain {executors}-launch.py trfolder:={name}
    """

    # Running the commands in the same shell instance
    process = subprocess.Popen(['/bin/bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    stdout, stderr = process.communicate(commands)# Send the commands to the bash process

    print(stdout) # Print the outputs and errors, if any
    if stderr:
        print("Errors:\n", stderr)

def main():
    path_config_cores_1 = "/home/lucian/simple-chain-ws/src/ros2-latency-analysis/simple-chain/config/two_nodes_1.yaml"
    path_config_cores_2 = "/home/lucian/simple-chain-ws/src/ros2-latency-analysis/simple-chain/config/two_nodes_2.yaml"
    path_config_payload = "/home/lucian/simple-chain-ws/src/ros2-latency-analysis/simple-chain/config/two_nodes_payload.yaml"
    
    core_config = [
        {'thread1': 1,'thread2': 1},
        {'thread1': 1,'thread2': 2},
    ]

    executor = "two_nodes_s1"
    for i in range(128, 500 * 1024 + 1, 128):
        size = ''

        if i < 1024:
            size = f"{i}B"  # Print in bytes
        else:
            size = f"{i / 1024:.2f}KB"  # Convert to KB and print

        name = f"{executor}-{size}"
        update_payload(path_config_payload, size)
        run_experiment(executor, name)
    
    executor = "two_nodes_m1"
    for i in range(128, 500 * 1024 + 1, 128):
        size = ''

        if i < 1024:
            size = f"{i}B"  # Print in bytes
        else:
            size = f"{i / 1024:.2f}KB"  # Convert to KB and print

        name = f"{executor}-{size}"
        update_payload(path_config_payload, size)
        run_experiment(executor, name)
    
    executor = "two_nodes_s2"
    for i in range(128, 500 * 1024 + 1, 128):
        size = ''

        if i < 1024:
            size = f"{i}B"  # Print in bytes
        else:
            size = f"{i / 1024:.2f}KB"  # Convert to KB and print

        for cc in core_config:
            name = f"{executor}-{size}-{cc[1]}"
            update_payload(path_config_payload, size)
            update_cores(path_config_cores_2, cores_string(cc[1]))
            run_experiment(executor, name)

    executor = "two_nodes_m2"
    for i in range(128, 500 * 1024 + 1, 128):
        size = ''

        if i < 1024:
            size = f"{i}B"  # Print in bytes
        else:
            size = f"{i / 1024:.2f}KB"  # Convert to KB and print

        for cc in core_config:
            name = f"{executor}-{size}-{cc[1]}"
            update_payload(path_config_payload, size)
            update_cores(path_config_cores_2, cores_string(cc[1]))
            run_experiment(executor, name)

main()