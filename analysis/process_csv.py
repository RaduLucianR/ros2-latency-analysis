import os
import re
import pandas as pd
import matplotlib.pyplot as plt

def process_and_plot(folder_path):
    # Dictionary to hold response times for each payload size, ensuring numeric sorting
    payload_data = {}

    for root, dirs, files in os.walk(folder_path):
        for dir_name in dirs:
            match = re.match(r'^two_nodes_(m2)-(\d+\.\d+)KB-(12)$', dir_name)
            if match:
                config, payload_str, setting = match.groups()
                payload_size = float(payload_str)
                csv_file_name = f"resp-time-{dir_name}.csv"
                csv_file_path = os.path.join(root, dir_name, csv_file_name)
                
                if payload_size % 5 == 0:
                    if os.path.isfile(csv_file_path):
                        df = pd.read_csv(csv_file_path)
                        # Convert response time from nanoseconds to milliseconds
                        response_times_ms = df['response_time'] / 10**6
                        filt = [time for time in response_times_ms if time < 10.00]
                        
                        if payload_size in payload_data:
                            payload_data[payload_size].extend(filt)
                        else:
                            payload_data[payload_size] = filt

    # Sort payloads and prepare data for plotting
    sorted_payloads = sorted(payload_data.keys())
    box_data = [payload_data[size] for size in sorted_payloads]
    labels = [str(size) for size in sorted_payloads]

    payload_sizes = []
    latencies = []
    for size, times in payload_data.items():
        payload_sizes.extend([size] * len(times))  # Repeat payload size for each latency measurement
        latencies.extend(times)

    # Plotting all box plots in one figure
    plt.figure(figsize=(20, 8))
    whis = 10
    # plt.scatter(payload_sizes, latencies, alpha=0.5)
    plt.boxplot(box_data, labels=labels, whis=whis) #whiskers set to 'whis' times the IQR
    plt.xticks(rotation=45)  # Rotate labels for readability
    # plt.title(f'RT by PS, 1 MTE for all tasks, whiskers {whis}x IQR')
    plt.title(f'RT by PS - one MTE for each tasks on more cores - whiskers {whis}x IQR')
    plt.xlabel('Payload Size (KB)')
    plt.ylabel('Response Time (ms)')
    plt.tight_layout()  # Adjust layout
    plt.savefig("/home/lucian/simple-chain-ws/src/ros2-latency-analysis/analysis/results/two-nodes/two_nodes_box_m2-12.png")
    plt.show()

# Replace 'your_folder_path' with the path to your folder containing the sub-folders
process_and_plot('/home/lucian/simple-chain-ws/graphs/two-nodes')
