import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch


# Read the CSV files
cores = ['111233', '111234', '112344', '123']
payloads = ['128B', '1KB', '10KB', '100KB', '500KB']
base_names = ['1-ste', '1-mte', 'n-ste', 'n-mte-per-1-node', 'n-mte-per-2-node']
leg = ['1-ste', '1-mte', \
       'n-ste-111233', \
       'n-ste-111234', \
       'n-ste-112344', \
       'n-mte-per-1-node-111233', \
       'n-mte-per-1-node-111234', \
       'n-mte-per-1-node-112344', \
       'n-mte-per-2-node']
base_path = '/home/lucian/simple-chain-ws/graphs'
# base_name = 'n-ste'

# Set up the figure and 3D axis
fig = plt.figure(figsize=(20, 18))
ax = fig.add_subplot(111, projection='3d')

# Setup colors for each executor
colors = ['r', 'g', 'b', 'c', 'gold', 'm', 'orange', 'pink', 'lime']
legend_elements = [Patch(facecolor=color, edgecolor='k', label=l) for color, l in zip(colors, leg)]

# Define the number of bins for the histogram
num_bins = 20

bar_width = 0.15
x_offset = np.array([
    -4*bar_width, -3*bar_width, -2*bar_width, -1*bar_width, 
    0, 
    1*bar_width, 2*bar_width, 3*bar_width, 4*bar_width
])


# Process each payload
for z, pl in enumerate(payloads):  # Using 'z' to place each payload along the z-axis
    histograms = []

    csv_paths = [
        f'{base_path}/{base_names[0]}-{pl}/resp-time-{base_names[0]}-{pl}.csv',
        f'{base_path}/{base_names[1]}-{pl}/resp-time-{base_names[1]}-{pl}.csv',
        f'{base_path}/{base_names[2]}-{pl}-{cores[0]}/resp-time-{base_names[2]}-{pl}-{cores[0]}.csv',
        f'{base_path}/{base_names[2]}-{pl}-{cores[1]}/resp-time-{base_names[2]}-{pl}-{cores[1]}.csv',
        f'{base_path}/{base_names[2]}-{pl}-{cores[2]}/resp-time-{base_names[2]}-{pl}-{cores[2]}.csv',
        f'{base_path}/{base_names[3]}-{pl}-{cores[0]}/resp-time-{base_names[3]}-{pl}-{cores[0]}.csv',
        f'{base_path}/{base_names[3]}-{pl}-{cores[1]}/resp-time-{base_names[3]}-{pl}-{cores[1]}.csv',
        f'{base_path}/{base_names[3]}-{pl}-{cores[2]}/resp-time-{base_names[3]}-{pl}-{cores[2]}.csv',
        f'{base_path}/{base_names[4]}-{pl}-{cores[3]}/resp-time-{base_names[4]}-{pl}-{cores[3]}.csv',
    ]

    for i, csv_path in enumerate(csv_paths):
        df = pd.read_csv(csv_path)
        response_times = df['response_time'] / 1_000_000
        hist, edges = np.histogram(response_times, bins=num_bins)
        x_positions = (edges[:-1] + edges[1:]) / 2 + x_offset[i]
        ax.bar(x_positions, hist, zs=z, zdir='y', width=bar_width, color=colors[i], edgecolor='k', alpha=0.7)

# Set the ticks for the y-axis (z-axis in the plot)
ax.set_yticks(range(len(payloads)))
ax.set_yticklabels(payloads)

# Labeling
ax.set_xlabel('Response Time (ms)')
ax.set_ylabel('Payload Size')
ax.set_zlabel('Number of Samples')

# Set title
ax.set_title('Response Time by Executor architecture, CPU configuration and Payload size')

# Set legend
ax.legend(handles=legend_elements, title="Executor architecture")

# Show plot
plt.show()
