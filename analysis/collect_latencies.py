import os
import re
import matplotlib.pyplot as plt

# Define the mapping for folder names to display names on the graph
name_mapping = {
    '1-ste': '1-ste',
    '1-mte': '1-mte',
    'n-ste-111233': 'n-ste-111233',
    'n-ste-111234': 'n-ste-111234',
    'n-ste-112344': 'n-ste-112344',
    'n-mte-per-1-node-111233': 'n-mte-per-1-node-111233',
    'n-mte-per-1-node-111234': 'n-mte-per-1-node-111234',
    'n-mte-per-1-node-112344': 'n-mte-per-1-node-112344',
    'n-mte-per-2-node-123': 'n-mte-per-2-node-123'
}

# Initialize a dictionary to hold the data
data = {name: {} for name in name_mapping.values()}

# List of payload sizes for ordering
payload_sizes = ['128B', '1KB', '10KB', '100KB', '500KB']

# Iterate over the folders and read the files
for folder in os.listdir('.'):
    for payload_size in payload_sizes:
        if payload_size in folder:
            file_name = f"cl-e2e-{folder}"
            try:
                with open(os.path.join(folder, file_name), 'r') as file:
                    contents = file.read()
                    max_time = float(re.search(r'max: (\d+\.\d+) ms', contents).group(1))
                    # Remove the payload size from the folder name for the legend
                    name_key = folder.replace('-' + payload_size, '')
                    for key in name_mapping:
                        if key in name_key:
                            data[name_mapping[key]].setdefault(payload_size, max_time)
            except FileNotFoundError:
                print(f"File {file_name} not found in folder {folder}")
            except AttributeError:
                print(f"Max time not found in file {file_name}")

# Plotting the data
plt.figure(figsize=(12, 6))
for name, timings in data.items():
    sorted_timings = sorted(timings.items(), key=lambda x: payload_sizes.index(x[0]))
    plt.plot([k for k, v in sorted_timings], [v for k, v in sorted_timings], label=name, marker='o')

plt.xlabel('Payload Size')
plt.ylabel('Response Time (ms)')
plt.title('Max Response Time vs Payload Size')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout(rect=[0,0,0.85,1])  # Adjust the rect parameter as needed
plt.grid(True)
plt.show()
