import os
import re
import matplotlib.pyplot as plt
import numpy as np

# Function to extract data from file
def extract_max_latency(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        match = re.search(r'max: ([\d.]+) ms', content)
        return float(match.group(1)) if match else None
    
def extract_avg_latency(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        match = re.search(r'avg: ([\d.]+) ms', content)
        return float(match.group(1)) if match else None

def filtr(latency):
    if latency > 500:
        return False

    return True
    
def check_config(tasks, execs, etypes, t2e, e2c):
    # if int(tasks) == 4:
    #     if e2c == "1" or e2c == "1-1" or e2c == "1-1-1-1":
    #         if all(char == 's' for char in etypes) or all(char == 'm' for char in etypes):
    #             return True

    # if int(tasks) == 6:
    #     if all(char == 's' for char in etypes) or all(char == 'm' for char in etypes):
    #         if all((char == '1' or char == '-') for char in e2c):
    #             return True
            
    # if int(tasks) == 6:
    #     if etypes == "22":
    #         if e2c == "1-1":
    #             return True

    
    stri = f"t{tasks}e{execs}_{etypes}_{t2e}_{e2c}"

    if stri in ["t10e3_ssm_1111111123_1-2-3", "t10e3_ssm_1111222333_1-2-3"]:
        return True
    
    return False

# Main function to process folders and plot data
def plot_lines(folder_path):
    data = {}
    ct2 = 0

    for root, dirs, files in os.walk(folder_path):
        for dir_name in dirs:
            # Adjusted regex to include s1 and m1 configurations
            match = re.match(r't(\d+)e(\d+)_([sm]+)_(\d+)_([\d-]+)_(\d+\.\d+)KB', dir_name)

            if match:
                tasks, execs, etypes, t2e, e2c, payload = match.groups()
                payload_value = float(payload[:-2])  # Convert payload size to float
                file_name = f"cl-e2e-{dir_name}"
                file_path = os.path.join(root, dir_name, file_name)

                if not os.path.isfile(file_path):
                    continue

                max_latency = extract_avg_latency(file_path)

                if max_latency is not None:
                    key = f"t{tasks}e{execs}_{etypes}_{t2e}_{e2c}"
                    
                    if key not in data.keys():
                        data[key] = []

                    if check_config(tasks, execs, etypes, t2e, e2c) and filtr(max_latency):
                        data[key].append((payload_value, max_latency))

    plt.figure(figsize=(15, 6))
    np.random.seed(398157)  # For reproducibility
    num_categories = 100
    colors = np.random.rand(num_categories, 3)
    ct = 0

    for config in data:
        if data[config]:
            payloads, latencies = zip(*sorted(data[config]))
            plt.scatter(payloads, latencies, label=config)
            plt.plot(payloads, latencies)
            ct += 1

    plt.title('Avg Latency vs Payload')
    plt.xlabel('Payload (KB)')
    plt.ylabel('Latency (ms)')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.subplots_adjust(right=0.75)
    plt.show()

plot_lines('/home/lucian/simple-chain-ws/graphs/two-ten-nodes-all')

