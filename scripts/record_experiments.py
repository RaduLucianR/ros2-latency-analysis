import subprocess
import yaml
import argparse
from exec_architectures import exec_architectures

def update_ps(file_path, yaml_obj, size):
    for exec in yaml_obj['executors']:
        for node in exec['nodes']:
            node['payload'] = size

    with open(file_path, 'w') as stream:
        yaml.dump(yaml_obj, stream, default_flow_style=False)

def check_tasks_unique_names(yaml_obj):
    names = set()

    for exec in yaml_obj['executors']:
        for task in exec['nodes']:
            if len(names) != 0:
                if task['name'] not in names:
                    names.add(task['name'])
                else:
                    raise ValueError(f"{task['name']} is duplicate! Nodes *must* have unique names")
            else:
                names.add(task['name'])

    return True


def name_details(yaml_obj):
    check_tasks_unique_names(yaml_obj)

    nrof_nodes = 0
    nrof_execs = len(yaml_obj['executors'])
    exec_str = ""
    t2e = ""
    exec_index = 1
    e2c = ""

    for exec in yaml_obj['executors']:
        nodes_of_exec = len(exec['nodes'])
        nrof_nodes += nodes_of_exec
        t2e += str(exec_index) * nodes_of_exec
        e2c += "".join(str(c) for c in exec['cores']) + "-"

        if exec['type'] == "single_threaded":
            exec_str = exec_str + "s"
        elif exec['type'] == "multi_threaded":
            exec_str = exec_str + "m"
        
        exec_index += 1

    if e2c[-1] == "-":
        e2c = e2c[0:-1]

    return f"t{nrof_nodes}e{nrof_execs}_{exec_str}_{t2e}_{e2c}"

def cores_string(core_values):
    concatenated_values = ""

    for value in core_values.values():
        concatenated_values += str(value)

    return concatenated_values

def run_experiment(executors, ros2_ws_name, name):
    commands = f"""
    source /opt/ros/humble/setup.bash
    source ~/ros2_caret_ws/install/local_setup.bash
    source ~/{ros2_ws_name}/install/local_setup.bash
    export LD_PRELOAD=$(readlink -f ~/ros2_caret_ws/install/caret_trace/lib/libcaret.so)
    ros2 launch simple-chain {executors}_launch.py trfolder:={name}
    """

    # Running the commands in the same shell instance
    process = subprocess.Popen(['/bin/bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    stdout, stderr = process.communicate(commands)# Send the commands to the bash process

    print(stdout) # Print the outputs and errors, if any
    if stderr:
        print("Errors:\n", stderr)

def main(config_path, ros2_ws_name, ps_start, ps_end, ps_step, overwrite_ps):
    archis = exec_architectures()
    ps_start *= 1024
    ps_end *=  1024
    ps_step *= 1024

    if overwrite_ps:
        for i in range(ps_start, ps_end, ps_step):
            size = ''

            if i < 1024:
                size = f"{i}B"  # Print in bytes
            else:
                size = f"{i / 1024:.2f}KB"  # Convert to KB and print

            for config in archis:
                details = name_details(config)
                name = f"{details}_{size}"
                # print(details)
                update_ps(config_path, config, size)
                run_experiment("exec_archi", ros2_ws_name, name)
    else:
        for config in archis:
            details = name_details(config)
            name = f"{details}_customPS"
            run_experiment("exec_archi", ros2_ws_name, name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Records experiments.")
    parser.add_argument("config_path", type=str, help="Config file path.")
    parser.add_argument("ros2_ws_name", type=str, help="Name of the ROS2 workspace, assuming it's in /home/$USER")
    parser.add_argument("--ps_start", type=int, default=10, help="Payload size (KB) start.")
    parser.add_argument("--ps_end", type=int, default=10, help="Payload size (KB) end.")
    parser.add_argument("--ps_step", type=int, default=10, help="Payload size (KB) step.")
    parser.add_argument("--overwrite_ps", type=bool, default=False, help="Overwrite payload sizes.")

    args = parser.parse_args()

    main(args.config_path, args.ros2_ws_name, args.ps_start, args.ps_end, args.ps_step, args.overwrite_ps)