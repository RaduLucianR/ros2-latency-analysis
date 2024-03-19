from caret_analyze import Application, Architecture, Lttng
from caret_analyze.plot import Plot, chain_latency
from caret_analyze.record import ResponseTime
from bokeh.plotting import figure, show
from bokeh.io import export_png
from caret_analyze.exceptions import ItemNotFoundError

import argparse
import os
from caret_analyze import Architecture
import subprocess

def proc_folder(trace_folder_path, trace_path_name, destination_path):
    lttng = Lttng(trace_folder_path)
    trace_folder_name = os.path.basename(trace_folder_path)
    archi_file = f"archi-{trace_folder_name}.yaml"
    parent_dir = os.path.dirname(trace_folder_path)
    arch = Architecture('yaml', f"{parent_dir}/{archi_file}")
    app = Application(arch, lttng)

    try:
        path = app.get_path(trace_path_name)
    except ItemNotFoundError:
        commands = f"""
        python3 /home/lucian/simple-chain-ws/src/ros2-latency-analysis/analysis/add-path-archi.py {trace_folder_path} /talker /listener target
        """

        # Running the commands in the same shell instance
        process = subprocess.Popen(['/bin/bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(commands)# Send the commands to the bash process
        print(stdout) # Print the outputs and errors, if any
        if stderr:
            print("Errors:\n", stderr)

        lttng = Lttng(trace_folder_path)
        trace_folder_name = os.path.basename(trace_folder_path)
        archi_file = f"archi-{trace_folder_name}.yaml"
        parent_dir = os.path.dirname(trace_folder_path)
        arch = Architecture('yaml', f"{parent_dir}/{archi_file}")
        app = Application(arch, lttng)
        path = app.get_path(trace_path_name)

    try:
        new_folder = os.path.join(destination_path, os.path.basename(trace_folder_path))
        os.makedirs(new_folder)
        print(f"Directory '{os.path.basename(trace_folder_path)}' created at '{new_folder}'")
    except FileExistsError:
        print(f"The directory '{os.path.basename(trace_folder_path)}' already exists at '{new_folder}'")

    # Chain latency graphs
    cl_node = chain_latency(path, granularity='node', lstrip_s=1, rstrip_s=1)
    cl_end_to_end = chain_latency(path, granularity='end-to-end', lstrip_s=1, rstrip_s=1)
    cl_node.render(filename = f'cl-node-{trace_folder_name}', directory = new_folder, format='png')
    cl_end_to_end.render(filename = f'cl-e2e-{trace_folder_name}', directory = new_folder, format='png')

    histogram = Plot.create_response_time_histogram_plot(path)
    histogram_fig = histogram.figure()
    export_png(histogram_fig, filename = f"{new_folder}/histo-{trace_folder_name}.png")

    stacked_bar = Plot.create_response_time_stacked_bar_plot(path)   
    stacked_bar_fig = stacked_bar.figure()
    export_png(stacked_bar_fig, filename = f"{new_folder}/stacked-{trace_folder_name}.png")

    message_flow_node = Plot.create_message_flow_plot(path, granularity='node', lstrip_s=1, rstrip_s=1)
    message_flow_node_fig = message_flow_node.figure()
    export_png(message_flow_node_fig, filename = f"{new_folder}/mf-node-{trace_folder_name}.png")

    message_flow_e2e = Plot.create_message_flow_plot(path, granularity='raw', lstrip_s=1, rstrip_s=1)
    message_flow_e2e_fig = message_flow_e2e.figure()
    export_png(message_flow_e2e_fig, filename = f"{new_folder}/mf-raw-{trace_folder_name}.png")

    cb_latency = Plot.create_latency_timeseries_plot(app.callbacks)
    cb_latency_fig = cb_latency.figure()
    export_png(cb_latency_fig, filename = f"{new_folder}/cb-lat-{trace_folder_name}.png")
    
    records = path.to_records()
    response = ResponseTime(records)
    response_time_records = response.to_all_records()
    response_df = response_time_records.to_dataframe()
    response_df.to_csv(f"{new_folder}/resp-time-{trace_folder_name}.csv")

def main(trace_folder_path, trace_path_name, destination_path, subfolders):
    visited = [folder.name for folder in os.scandir(destination_path) if folder.is_dir()]

    if subfolders:
        for item in os.listdir(trace_folder_path):
            full_path = os.path.join(trace_folder_path, item)

            if os.path.isdir(full_path) and (os.path.basename(full_path) not in visited):
                proc_folder(full_path, trace_path_name, destination_path)
                # print(os.path.basename(full_path))
    else:
        proc_folder(trace_folder_path, trace_path_name, destination_path)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get and save plots and data for a trace folder.")
    parser.add_argument("trace_folder_path", type=str, help="Path to the trace folder, or to a folder containing trace sub-folders. \
                        Assuming its respective architecture yaml file is in the parent directory of the trace (sub-)folder.")
    parser.add_argument("trace_path_name", type=str, help="The name of the trace path from the architecture file \
                        for which the plots are needed.")
    parser.add_argument("destination_path", type=str, help="Path to the folder used for storing the plots and data.")
    parser.add_argument("--subfolders", type=bool, default=False, help="Process subfolders on the path")

    args = parser.parse_args()

    main(args.trace_folder_path, args.trace_path_name, args.destination_path, args.subfolders)
