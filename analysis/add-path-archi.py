import argparse
import os
from caret_analyze import Architecture

def main(archi_path, source_node, dest_node, name, context_t):
    archi_file = f"archi-{os.path.basename(archi_path)}.yaml"
    parent_dir = os.path.dirname(archi_path)
    arch = Architecture('yaml', f"{parent_dir}/{archi_file}")

    # Get a list of all possible paths between source and destination nodes
    paths = arch.search_paths(source_node, dest_node) 

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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script to add an end-to-end path \
                                        for analysis to a CARET architecture file.")
    parser.add_argument("archi_path", type=str, help="Path to the trace folder. \
                        Assuming the architecture yaml file is in the parent directory of the trace folder.")
    parser.add_argument("source_node", type=str, help="Start node of the end-to-end path. \
                            A node's name must have a preceeding slash    /   !!!")
    parser.add_argument("dest_node", type=str, help="End node of the trace path")
    parser.add_argument("name", type=str, help="Desired name for the added trace path")
    parser.add_argument("--context_type", type=str, default="use_latest_message", help="CARET context type for intra-node communication. \
                        Choose between use_latest_message or callback_chain. Default is use_latest_message!!!!")

    args = parser.parse_args()

    main(args.archi_path, args.source_node, args.dest_node, args.name, args.context_type)
