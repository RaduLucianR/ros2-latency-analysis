usage() {
    echo "Create CARET architecture files for every trace sub-folder of the given folder."
    echo "Usage: $0 [<folder_with_trace_subfolders>]"
    exit 1
}

# Check if at least one argument is provided
if [ $# -eq 0 ]; then
    usage
fi

destination_folder=$1

for subdir in "$destination_folder"/*; do
    # Check if the item is a directory
    if [ -d "$subdir" ]; then
        echo "Processing trace folder: $subdir"
        subdir_f="${subdir##*/}"

        if [[ -f "${destination_folder}/archi-${subdir_f}.yaml" ]]; then
            continue
        fi

        ros2 caret create_architecture_file ${subdir} -o ${destination_folder}/archi-${subdir_f}.yaml
    fi
done