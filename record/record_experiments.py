import subprocess
import yaml
import argparse
from exec_architectures import exec_architectures
from execarchi_from_string import execarchi_from_string

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
    # exp_list = [
    #     "t2e2_mm_12_1-2",
    #     "t2e2_sm_12_1-2",
    #     "t2e2_sm_12_1-2",
    #     "t2e2_mm_12_1-2",
    #     "t2e2_ss_12_1-2",
    #     "t2e2_ss_12_1-2",
    #     "t2e2_mm_12_1-2",
    #     "t2e1_s_11_1",
    #     "t2e2_sm_12_1-2",
    #     "t2e2_ss_12_1-2",
    #     "t3e2_ms_112_1-2",
    #     "t3e2_mm_112_1-1",
    #     "t3e3_ssm_123_1-2-3",
    #     "t3e2_ss_112_1-1",
    #     "t3e2_mm_112_1-1",
    #     "t3e3_ssm_123_1-1-1",
    #     "t3e3_ssm_123_1-1-1",
    #     "t3e2_sm_112_1-2",
    #     "t3e3_sss_123_1-1-1",
    #     "t3e2_mm_112_1-1",
    #     "t4e2_ss_1112_1-1",
    #     "t4e2_ss_1112_1-2",
    #     "t4e2_ss_1112_1-2",
    #     "t4e2_mm_1112_1-2",
    #     "t4e2_sm_1112_1-2",
    #     "t4e2_ss_1122_1-1",
    #     "t4e2_ms_1112_1-1",
    #     "t4e1_m_1111_1",
    #     "t4e2_sm_1122_1-2",
    #     "t4e2_ss_1122_1-2",
    #     "t5e3_mms_11223_1-1-1",
    #     "t5e1_s_11111_1",
    #     "t5e3_ssm_11123_1-2-3",
    #     "t5e3_sss_11223_1-1-1",
    #     "t5e3_ssm_11123_1-2-2",
    #     "t5e3_mmm_11123_1-2-3",
    #     "t5e3_ssm_11223_1-2-3",
    #     "t5e3_ssm_11123_1-2-3",
    #     "t5e1_m_11111_1",
    #     "t5e1_s_11111_1",
    #     "t6e3_mmm_112233_1-1-2",
    #     "t6e2_sm_111112_1-1",
    #     "t6e2_ss_111112_1-1",
    #     "t6e3_mms_111123_1-2-2",
    #     "t6e2_mm_111122_1-1",
    #     "t6e2_ms_111122_1-1",
    #     "t6e2_ms_111112_1-2",
    #     "t6e2_ms_111122_1-1",
    #     "t6e2_sm_111222_1-1",
    #     "t6e3_ssm_111123_1-2-3",
    #     "t7e3_mmm_1111123_1-2-2",
    #     "t7e3_sss_1111123_1-2-3",
    #     "t7e3_ssm_1111123_1-2-3",
    #     "t7e1_s_1111111_1",
    #     "t7e3_ssm_1111123_1-2-3",
    #     "t7e5_mmmss_1122345_1-1-1-1-1",
    #     "t7e1_m_1111111_1",
    #     "t7e3_ssm_1111123_1-1-1",
    #     "t7e3_sss_1111123_1-2-3",
    #     "t7e3_sss_1111123_1-2-2",
    #     "t8e4_ssss_11111234_1-1-2-3",
    #     "t8e4_ssmm_11111234_1-1-2-3",
    #     "t8e1_s_11111111_1",
    #     "t8e2_mm_11112222_1-2",
    #     "t8e2_sm_11111122_1-2",
    #     "t8e2_ss_11111122_1-2",
    #     "t8e1_m_11111111_1",
    #     "t8e2_sm_11111122_1-2",
    #     "t8e4_ssmm_11223344_1-1-1-1",
    #     "t8e4_ssss_11111234_1-2-2-2",
    #     "t9e3_mmm_111122233_1-1-1",
    #     "t9e3_mmm_111111123_1-2-2",
    #     "t9e1_m_111111111_1",
    #     "t9e3_mms_111122233_1-2-3",
    #     "t9e3_mmm_111111123_1-1-1",
    #     "t9e3_sss_111111123_1-2-2",
    #     "t9e1_s_111111111_1",
    #     "t9e6_ssssss_111123456_1-1-2-2-2-2",
    #     "t9e3_sss_111111123_1-2-3",
    #     "t9e3_sss_111111123_1-2-3",
    #     "t10e3_ssm_1111111123_1-1-1",
    #     "t10e1_s_1111111111_1",
    #     "t10e3_mms_1111111123_1-1-1",
    #     "t10e3_sss_1111111123_1-2-2",
    #     "t10e1_s_1111111111_1",
    #     "t10e3_mmm_1111222333_1-2-3",
    #     "t10e3_sss_1111111123_1-2-3",
    #     "t10e3_ssm_1111111123_1-2-3",
    #     "t10e1_s_1111111111_1",
    #     "t10e3_sss_1111111123_1-2-2"
    # ]
    exp_list = [
        "t2e2_sm_12_1-2",
        "t2e2_mm_12_1-2",
        "t2e2_sm_12_1-2",
        "t3e2_ms_112_1-2",
        "t3e2_mm_112_1-1",
        "t3e2_sm_112_1-2",
        "t3e2_ss_112_1-1",
        "t4e2_ss_1112_1-2",
        "t4e2_sm_1112_1-2",
        "t4e2_ss_1112_1-1",
        "t5e1_m_11111_1",
        "t5e1_s_11111_1",
        "t5e2_ss_11112_1-1",
        "t5e2_ss_11112_1-2",
        "t6e2_sm_111112_1-1",
        "t6e2_ms_111112_1-2",
        "t6e2_ss_111112_1-1",
        "t7e1_m_1111111_1",
        "t7e1_s_1111111_1",
        "t7e2_ss_1111112_1-1",
        "t7e2_sm_1111112_1-1",
        "t7e2_ss_1111112_1-2",
        "t7e2_sm_1111112_1-2",
        "t7e3_ssm_1111123_1-2-3",
        "t7e3_ssm_1111123_1-1-1",
        "t7e3_ssm_1111123_1-2-2",
        "t7e1_s_1111111_1",
        "t8e1_s_11111111_1",
        "t8e2_ss_11111122_1-2",
        "t8e2_sm_11111122_1-2",
        "t8e1_m_11111111_1",
        "t9e1_m_111111111_1",
        "t9e1_s_111111111_1",
        "t9e2_ss_111111122_1-1",
        "t9e2_ss_111111122_1-2",
        "t9e2_ss_111111112_1-1",
        "t9e2_ss_111111112_1-2",
        "t9e2_ms_111111112_1-2",
        "t9e2_ss_111112222_1-1",
        "t9e2_ss_111112222_1-2",
        "t9e3_sss_111111123_1-2-2",
        "t9e3_sss_111111123_1-2-3",
        "t10e3_ssm_1111111123_1-2-3",
        "t10e3_ssm_1111111123_1-1-1",
        "t10e3_sss_1111111123_1-2-3",
        "t10e3_sss_1111111123_1-2-2",
        "t10e2_ss_1111111112_1-1",
        "t10e2_ss_1111111112_1-2",
        "t10e2_ss_1111122222_1-2",
        "t10e2_sm_1111122222_1-2",
        "t10e1_s_1111111111_1",
        "t10e1_m_1111111111_1",
    ]
    # archis = exec_architectures()
    archis = []

    for exp in exp_list:
        archis.append(execarchi_from_string(exp))

    ps_start *= 1024
    ps_end *=  1024
    ps_step *= 1024

    if overwrite_ps:
        for i in range(ps_start, ps_end, ps_step):
            size = ''

            for j in range(20, 200 + 1, 20):
                if i < 1024:
                    size = f"{i}B"  # Print in bytes
                else:
                    size = f"{(i + j * 1024) / 1024:.2f}KB"  # Convert to KB and print

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
    parser.add_argument("config_path", type=str, help="Path to the YAML file that defines the Executor Architecture.")
    parser.add_argument("ros2_ws_name", type=str, help="Name of the ROS2 workspace, assuming it's in /home/$USER")
    parser.add_argument("--ps_start", type=int, default=10, help="Payload size (KB) start.")
    parser.add_argument("--ps_end", type=int, default=10, help="Payload size (KB) end.")
    parser.add_argument("--ps_step", type=int, default=10, help="Payload size (KB) step.")
    parser.add_argument("--overwrite_ps", type=bool, default=False, help="Overwrite payload sizes.")

    args = parser.parse_args()

    main(args.config_path, args.ros2_ws_name, args.ps_start, args.ps_end, args.ps_step, args.overwrite_ps)