import os
import re
import matplotlib.pyplot as plt
import numpy as np

def filt(data, thersh):
    return {config: [(payload, latency) for payload, latency in pairs if latency <= thersh] for config, pairs in data.items()}

def filt_s1(data):
    return {config: [(payload, latency) for payload, latency in pairs if payload % 5 == 0] for config, pairs in data.items()}


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

# Function to plot data
def plot_data(data, title, filename):
    if data:
        payloads, latencies = zip(*sorted(data))
        plt.figure(figsize=(10, 6))
        plt.scatter(payloads, latencies)
        plt.title(title)
        plt.xlabel('Payload (KB)')
        plt.ylabel('Latency (ms)')
        plt.xticks(range(0, 601, 20))  # Granularity of 20KB
        plt.savefig(filename)
        plt.show()

# Main function to process folders and plot data
def process_and_plot(folder_path):
    # Extended to include s1 and m1 configurations
    data = {'t2': [], 
            't3': [], 
            't4': [], 
            't5': [], 
            't6': [], 
            't7': [],
            't8': [],
            't9': [],
            't10': []
            }

    for root, dirs, files in os.walk(folder_path):
        for dir_name in dirs:
            # Adjusted regex to include s1 and m1 configurations
            match = re.match(r't(\d+)e(\d+)_(s|m)+_(\d+)_(\d+)_(\d+\.\d+)KB', dir_name)
            if match:
                tasks, execs, etypes, t2e, e2c, payload = match.groups()
                payload_value = float(payload[:-2])  # Convert payload size to float
                file_name = f"cl-e2e-{dir_name}"
                max_latency = extract_max_latency(os.path.join(root, dir_name, file_name))

                if max_latency is not None:
                    key = f"t{tasks}"
                    data[key].append((payload_value, max_latency))

    plt.figure(figsize=(15, 9))
    # colors = ['blue', 'red', 'green', 'orange', 'purple', 'grey']
    ct = 0

    for config in data:
        if data[config]:
            payloads, latencies = zip(*sorted(data[config]))
            payloads_array = np.array(payloads)
            latencies_array = np.array(latencies)
            slope, intercept = np.polyfit(payloads_array, latencies_array, 1)
            trendline = slope * payloads_array + intercept
            # plt.plot(payloads_array, trendline, color=colors[ct], lw=3)  # Plotting the trend line
            plt.scatter(payloads, latencies, label=config)
        
    plt.title('Max Latency vs Payload')
    plt.xlabel('Payload (KB)')
    plt.ylabel('Latency (ms)')
    plt.legend()
    plt.xticks(range(0, 1000, 10))  # Granularity of 20KB
    name = "two-ten-nodes-1mte2cores"
    # plt.savefig(f"/home/lucian/simple-chain-ws/src/ros2-latency-analysis/analysis/results/{name}.png")
    plt.show()

# Replace 'your_folder_path' with the path to your folder containing the sub-folders
process_and_plot('/home/lucian/simple-chain-ws/graphs/two-six-nodes-mte')
