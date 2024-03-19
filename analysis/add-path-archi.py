import argparse
import os
from caret_analyze import Architecture
from caret_analyze.exceptions import ItemNotFoundError

def proc_folder(path_folder, source_node, dest_node, name, context_t):
    archi_file = f"archi-{os.path.basename(path_folder)}.yaml"
    parent_dir = os.path.dirname(path_folder)
    arch = Architecture('yaml', f"{parent_dir}/{archi_file}")
    paths = []
    # Get a list of all possible paths between source and destination nodes
    try:
        paths = arch.search_paths(source_node, dest_node) 
    except ItemNotFoundError:
        print(f"Oops, {archi_file} doesn't have the {source_node} or {dest_node}")

    # Select the first path from the list. This assumes that there is ONLY ONE
    # possible path between the source and destination nodes!!!
    # This might NOT be the case!!! For our purposes this is fine, but beware!
    path = paths[0]

    arch.add_path(name, path)
    arch.export(f"{parent_dir}/{archi_file}", force = True) # Overwrite existent architecture file

    with open(f"{parent_dir}/{archi_file}", 'r') as file:
        file_contents = file.read()

    # Replace null contexts with the desired context type. Default is use_latest_message
    file_contents = file_contents.replace("context_type: UNDEFINED", f'context_type: {context_t}')

    # Write the changes back to the file
    with open(f"{parent_dir}/{archi_file}", 'w') as file:
        file.write(file_contents)

def main(path, source_node, dest_node, name, context_t, subfolders):
    if subfolders:
        for item in os.listdir(path):
            full_path = os.path.join(path, item)

            if os.path.isdir(full_path):
                proc_folder(full_path, source_node, dest_node, name, context_t)
    else:
        proc_folder(path, source_node, dest_node, name, context_t)
                


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script to add an end-to-end path \
                                        for analysis to a CARET architecture file.")
    parser.add_argument("path_folder", type=str, help="Path to a trace folder, or to a folder of trace sub-folders. \
                        Assuming the architecture yaml file is in the parent directory of the trace (sub-)folder. ")
    parser.add_argument("source_node", type=str, help="Start node of the end-to-end path. \
                            A node's name must have a preceeding slash    /   !!!")
    parser.add_argument("dest_node", type=str, help="End node of the trace path")
    parser.add_argument("name", type=str, help="Desired name for the added trace path")
    parser.add_argument("--context_type", type=str, default="use_latest_message", help="CARET context type for intra-node communication. \
                        Choose between use_latest_message or callback_chain. Default is use_latest_message!!!!")
    parser.add_argument("--subfolders", type=bool, default=False, help="Process all subfolders on path.")

    args = parser.parse_args()

    main(args.path_folder, args.source_node, args.dest_node, args.name, args.context_type, args.subfolders)