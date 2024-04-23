import os
import re
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from matplotlib.patches import Patch
import random
import csv
# from mpl_toolkits.mplot3d import Axes3D

def is_valid_folder(folder_name):
    regex = r"t(\d+)e(\d+)_([sm]+)_(\d+)_([\d-]+)_(\d+\.\d+)KB"
    match = re.match(regex, folder_name)
    if match:
        tasks, execs, etypes, t2e, e2c, payload = match.groups()
        tasks = int(tasks)
        execs = int(execs)
        # Check for all ones in e2c
        # if all((c == '1' or c == '2') for c in e2c if c.isdigit()):
            # Check for only s or m in etypes and exactly 'tasks' tasks
        stri = f"t{tasks}e{execs}_{etypes}_{t2e}_{e2c}"

        if tasks == 9 and execs == 3 and etypes == "sss" and t2e == "111111123":
        # if stri in [
        #     #### GOOD CONFIGS
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
            
        #     #### BAD CONFIGS
        #     "t8e8_mmmmmmmm_12345678_1-1-1-1-2-2-2-2"
        # ]:
            return True, payload
            
    return False, None

def get_folders(base_path):
    valid_folders = {}
    for folder in os.listdir(base_path):
        is_valid, payload = is_valid_folder(folder)
        # print(is_valid)
        if is_valid:
            if payload not in valid_folders:
                valid_folders[payload] = []
            valid_folders[payload].append(folder)
    return valid_folders

def read_and_plot_histograms(base_path, folders_by_payload):
    for payload, folders in folders_by_payload.items():
        plt.figure(figsize=(10, 6))  # You can adjust the size as needed
        colors = cm.get_cmap('nipy_spectral', len(folders))  # Get a colormap with as many colors as there are folders

        for i, folder in enumerate(folders):
            csv_path = os.path.join(base_path, folder, f'resp-time-{folder}.csv')
            try:
                threshold_ms = 200
                data = pd.read_csv(csv_path)
                filtered_data = data['response_time'] / 1_000_000
                filtered_data = filtered_data[filtered_data < threshold_ms]
                plt.hist(filtered_data, bins=25, alpha=0.7, color=colors(i), label=f'Config {folder}')
            except FileNotFoundError:
                print(f"File not found: {csv_path}")
            except Exception as e:
                print(f"An error occurred while processing {csv_path}: {e}")

        plt.title(f'Response Time Histograms for Payload {payload} KB')
        plt.xlabel('Response Time (ms)')
        plt.ylabel('Number of samples')
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
        plt.subplots_adjust(right=0.75)
        plt.show()

def plot_3d_histogram(base_path, folders_by_payload):
    fig = plt.figure(figsize=(14, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(elev=30, azim=45)

    # Collect all unique configurations and assign a color to each
    all_folders = set(folder for payload_folders in folders_by_payload.values() for folder in payload_folders)
    color_map = cm.get_cmap('nipy_spectral', len(all_folders))
    stripped = [re.sub('\_(\d+\.\d+)KB$', '', fol) for i, fol in enumerate(sorted(all_folders))]
    folder_colors = {folder: (random.random(), random.random(), random.random()) for folder in stripped}

    # folder_colors = {}
    # i = 0

    # for folder in stripped:
    #     folder_colors[folder] = color_map(i)
    #     i += 1

    payloads = sorted(folders_by_payload.keys(), key=float)

    '''
    Boundries to see the minimum latency
    t2: [0.2, 0.4]
    t3: [15, 20]
    t4: [31, 36]
    t5: [47, 52]
    t6: [63, 69]
    t7: [83, 88]
    t8: [100, 106]
    t9: [121, 127]
    t10: [140, 150]
    '''
    min_latency = 121  # Minimum response time in ms to display
    max_latency = 140 # Maximum response time in ms to display

    legend_handles = {}

    for z, payload in enumerate(payloads):
        folders = folders_by_payload[payload]

        for folder in folders:
            folder_stripped = re.sub('\_(\d+\.\d+)KB$', '', folder)
            color = folder_colors[folder_stripped]  # Use the consistent color for this folder
            csv_path = os.path.join(base_path, folder, f'resp-time-{folder}.csv')

            try:
                data = pd.read_csv(csv_path)
                response_time_ms = data['response_time'] / 1_000_000

                # Check if all points are strictly within the desired range
                if response_time_ms.between(min_latency, max_latency).all():
                    # Histogram with specified range
                    hist, bins = np.histogram(response_time_ms, bins=20)
                    width = (bins[1] - bins[0]) * 0.8
                    center = (bins[:-1] + bins[1:]) / 2
                    
                    ax.bar(center, hist, zs=z, zdir='y', width=width, alpha=0.9, color=color)

                    if folder_stripped not in legend_handles:
                        legend_handles[folder_stripped] = Patch(color=color, label=folder_stripped)

            except FileNotFoundError:
                continue
            except Exception as e:
                print(f"An error occurred while processing {csv_path}: {e}")

    ax.set_xlabel('Response Time (ms)')
    ax.set_xlim(min_latency, max_latency)
    ax.set_ylabel('Payload (KB)')
    ax.set_zlabel('Frequency')
    ax.set_yticks(range(len(payloads)))
    ax.set_yticklabels([f'{p}' for p in payloads])

    # Add the legend using the unique Patch objects created
    ax.legend(handles=list(legend_handles.values()), bbox_to_anchor=(1.1, 1.05))
    plt.show()

def find_best_config(base_path, folders_by_payload):
    payloads = sorted(folders_by_payload.keys(), key=float)

    for z, payload in enumerate(payloads):
        folders = folders_by_payload[payload]
        min_latency_over_payload = 0
        best_config = ""

        for folder in folders:
            csv_path = os.path.join(base_path, folder, f'resp-time-{folder}.csv')

            try:
                data = pd.read_csv(csv_path)
                response_time_ms = data['response_time'] / 1_000_000
                avg = response_time_ms.mean()

                if avg > min_latency_over_payload:
                    min_latency_over_payload = avg
                    best_config = re.sub('\_(\d+\.\d+)KB$', '', folder)
            except FileNotFoundError:
                continue
        
        print(f"{payload}KB: {best_config}")

        with open('top_configs_over_tasks_and_payload.csv','a') as fd:
            fd.write(f"{payload}KB, {best_config}\n")

base_path = '/home/lucian/simple-chain-ws/graphs/two-ten-nodes-all'
folders_by_payload = get_folders(base_path)
# read_and_plot_histograms(base_path, folders_by_payload)
plot_3d_histogram(base_path, folders_by_payload)
# find_best_config(base_path, folders_by_payload)