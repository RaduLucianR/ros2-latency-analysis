import os

# Path to your directory
directory_path = '/home/lucian/simple-chain-ws/graphs/two-ten-nodes-all'

# List to hold the names of all empty top-level sub-folders
empty_subfolders = []

# Iterate over each item in the directory
for name in os.listdir(directory_path):
    # Full path of the item
    full_path = os.path.join(directory_path, name)
    # Check if the item is a directory and if it's empty
    if os.path.isdir(full_path) and not os.listdir(full_path):
        empty_subfolders.append(name)

print(*empty_subfolders, sep="\n")
