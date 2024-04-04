import subprocess
import yaml

def update_yaml(file_path, new_data):
    # Overwrite the YAML file with the new data
    with open(file_path, 'w') as stream:
        yaml.dump(new_data, stream, default_flow_style=False)

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
    ros2 launch simple-chain {executors}_launch.py trfolder:={name}
    """

    # Running the commands in the same shell instance
    process = subprocess.Popen(['/bin/bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    stdout, stderr = process.communicate(commands)# Send the commands to the bash process

    print(stdout) # Print the outputs and errors, if any
    if stderr:
        print("Errors:\n", stderr)

def main():
    base_path = "/home/pi/ros_ws/src/ros2-latency-analysis/simple-chain/config/"
    path_config = "/home/pi/ros_ws/src/ros2-latency-analysis/simple-chain/config/executor_architecture_template.yaml"

    r_start = 5 * 1024
    r_end = 990 * 1024
    r_step = 10 * 1024

    for i in range(r_start, r_end, r_step):
        size = ''

        if i < 1024:
            size = f"{i}B"  # Print in bytes
        else:
            size = f"{i / 1024:.2f}KB"  # Convert to KB and print

        data1 = {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1, 2],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": size},
                        {"name": "node2", "subscribe": "topic1", "publish": "NONE", "payload": size},
                    ],
                }
            ]
        }

        data2 = {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1, 2],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": size},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": size},
                        {"name": "node3", "subscribe": "topic2", "publish": "NONE", "payload": size},
                    ],
                }
            ]
        }

        data3 = {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1, 2],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": size},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": size},
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": size},
                        {"name": "node4", "subscribe": "topic3", "publish": "NONE", "payload": size},
                    ],
                }
            ]
        }

        data4 = {
            "executors": [
                {
                    "name": "executor1",
                    "type": "multi_threaded",
                    "cores": [1, 2],
                    "nodes": [
                        {"name": "node1", "subscribe": "NONE", "publish": "topic1", "payload": size},
                        {"name": "node2", "subscribe": "topic1", "publish": "topic2", "payload": size},
                        {"name": "node3", "subscribe": "topic2", "publish": "topic3", "payload": size},
                        {"name": "node4", "subscribe": "topic3", "publish": "topic4", "payload": size},
                        {"name": "node5", "subscribe": "topic4", "publish": "NONE", "payload": size},
                    ],
                }
            ]
        }

        data = [data1, data2, data3, data4]
        nrof_tasks = 2

        for d in data:
            name = f"tasks_{nrof_tasks}_1mte12_{size}"
            update_yaml(path_config, d)
            run_experiment("exec_archi", name)
            nrof_tasks = nrof_tasks + 1

main()