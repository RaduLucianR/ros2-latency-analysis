# big 2-tuple list [cpu-setting, payload-setting]

# for 
#   modify cpu.yaml
#   modify msg_sizes.yaml
#   ros2 launch simple-chain 1-ste trfolder:=<name>

import subprocess
import yaml

def update_payload(file_path, new_size):
    # Load the YAML file
    with open(file_path, 'r') as stream:
        data = yaml.safe_load(stream)

    # Update the message_size for each specified key
    keys_to_update = ['/camera', '/fusion', '/perception', '/planning', '/control']
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
    source ~/simple-chain-ws/install/local_setup.bash
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
    path_config_cores_1 = "/home/lucian/simple-chain-ws/src/ros2-latency-analysis/simple-chain/config/exec-cpu-n-per-1-node.yaml"
    path_config_cores_2 = "/home/lucian/simple-chain-ws/src/ros2-latency-analysis/simple-chain/config/exec-cpu-n-mte-per-2-node.yaml"
    path_config_payload = "/home/lucian/simple-chain-ws/src/ros2-latency-analysis/simple-chain/config/msg_sizes.yaml"

    settings_1 = [
        ("128B"),
        ("1KB"),
        ("10KB"),
        ("100KB"),
        ("500KB"),
    ]

    settings_n_1 = [
        ("128B", {'thread1': 1,'thread2': 1,'thread3': 2,'thread4': 3,'thread5': 4,'thread6': 4}),
        ("1KB", {'thread1': 1,'thread2': 1,'thread3': 2,'thread4': 3,'thread5': 4,'thread6': 4}),
        ("10KB", {'thread1': 1,'thread2': 1,'thread3': 2,'thread4': 3,'thread5': 4,'thread6': 4}),
        ("100KB", {'thread1': 1,'thread2': 1,'thread3': 2,'thread4': 3,'thread5': 4,'thread6': 4}),
        ("500KB", {'thread1': 1,'thread2': 1,'thread3': 2,'thread4': 3,'thread5': 4,'thread6': 4}),

        ("128B", {'thread1': 1,'thread2': 1,'thread3': 1,'thread4': 2,'thread5': 3,'thread6': 4}),
        ("1KB", {'thread1': 1,'thread2': 1,'thread3': 1,'thread4': 2,'thread5': 3,'thread6': 4}),
        ("10KB", {'thread1': 1,'thread2': 1,'thread3': 1,'thread4': 2,'thread5': 3,'thread6': 4}),
        ("100KB", {'thread1': 1,'thread2': 1,'thread3': 1,'thread4': 2,'thread5': 3,'thread6': 4}),
        ("500KB", {'thread1': 1,'thread2': 1,'thread3': 1,'thread4': 2,'thread5': 3,'thread6': 4}),

        ("128B", {'thread1': 1,'thread2': 1,'thread3': 1,'thread4': 2,'thread5': 3,'thread6': 3}),
        ("1KB", {'thread1': 1,'thread2': 1,'thread3': 1,'thread4': 2,'thread5': 3,'thread6': 3}),
        ("10KB", {'thread1': 1,'thread2': 1,'thread3': 1,'thread4': 2,'thread5': 3,'thread6': 3}),
        ("100KB", {'thread1': 1,'thread2': 1,'thread3': 1,'thread4': 2,'thread5': 3,'thread6': 3}),
        ("500KB", {'thread1': 1,'thread2': 1,'thread3': 1,'thread4': 2,'thread5': 3,'thread6': 3}),
    ]
    
    settings_n_2 = [
        ("128B", {'thread1': 1,'thread2': 2,'thread3': 3}),
        ("1KB", {'thread1': 1,'thread2': 2,'thread3': 3}),
        ("10KB", {'thread1': 1,'thread2': 2,'thread3': 3}),
        ("100KB", {'thread1': 1,'thread2': 2,'thread3': 3}),
        ("500KB", {'thread1': 1,'thread2': 2,'thread3': 3}),
    ]

    executor = "1-ste"
    for tup in settings_1:
        name = f"{executor}-{tup}"
        update_payload(path_config_payload, tup)
        run_experiment(executor, name)

    executor = "1-mte"
    for tup in settings_1:
        name = f"{executor}-{tup}"
        update_payload(path_config_payload, tup)
        run_experiment(executor, name)

    executor = "n-ste"
    for tup in settings_n_1:
        name = f"{executor}-{tup[0]}-{cores_string(tup[1])}"
        update_payload(path_config_payload, tup[0])
        update_cores(path_config_cores_1, tup[1])
        run_experiment(executor, name)
    
    executor = "n-mte-per-1-node"
    for tup in settings_n_1:
        name = f"{executor}-{tup[0]}-{cores_string(tup[1])}"
        update_payload(path_config_payload, tup[0])
        update_cores(path_config_cores_1, tup[1])
        run_experiment(executor, name)

    executor = "n-mte-per-2-node"
    for tup in settings_n_2:
        name = f"{executor}-{tup[0]}-{cores_string(tup[1])}"
        update_payload(path_config_payload, tup[0])
        update_cores(path_config_cores_1, tup[1])
        run_experiment(executor, name)
    


main()