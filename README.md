# Latency analysis library for ROS2

### Introduction
This library uses CARET (repository [here](https://github.com/tier4/caret?tab=readme-ov-file), documentation [here](https://tier4.github.io/caret_doc/main/), paper [here](https://ieeexplore.ieee.org/document/10086380)), a library for measuring end-to-end latency in ROS2 systems. The details of the installation can be found [here](https://tier4.github.io/caret_doc/main/installation/installation/), while a script that *should* do this automatically for you is provided [here](https://github.com/RaduLucianR/ros2-latency-analysis/blob/main/scripts/install_caret.bash). 

The ROS2 workspace that you are working in must be built with CARET. **Every time you modify the ROS2 workspace, you must build the project with CARET. This can be done with the following command:
```
colcon build --symlink-install --cmake-args -DBUILD_TESTING=OFF
```

CARET uses the [Linux traces](https://lttng.org/) under the hood, which are also used by Linux to record events (irespective of ROS2). Since CARET is built with your ROS2 workspace, CARET will start to record traces every time you start a ROS2 process. When you kill the ROS2 process, CARET stops recording traces and saves them in a folder, by default as a sub-folder of `~/.ros/tracing`. The created folder with traces contains information about each generated trace. CARET uses many samples to create a distribution of the latencies. After recording, CARET requires a special `.yaml` file to be made for a trace folder which is called "architecture file". This architecture file contains details about the nodes, their publishing/subscription topics and which executors they belong to. After the architecture file is created, the user needs to manually write in the architecture file the path of the ROS2 graph for which they want to find the end-to-end latency. Then, CARET offers functions to calculate the end-to-end latency, generate a .csv with all samples and also plot them. All these steps are required for **only one** set of initial values in ROS2. Thus, if one wants to test more initial values, then these steps must be automated, and this is what this library does. The flow of the library is illustrated in the figure below:

<p align="center">
  <img src="https://github.com/RaduLucianR/ros2-latency-analysis/assets/57638808/47271864-ee43-496a-be08-c6fe295bbaed" />
</p>

### Steps
1. Record experiments with the [`record_experiments.py`](https://github.com/RaduLucianR/ros2-latency-analysis/blob/main/record/record_experiments.py) script from the `record` folder:
   ```
   python3 record_experiments.py /path/to/yaml/file/with/executor/config <name_of_working_ros2_workspace>
   ```
  
   You may modify the `record_experiments.py` file to run experiments for whatever executor configuration you want. More about how to create an executor configuration below. The `record_experiments.py` script does two things:
   - Store the desired executor configurations in a data structure
   - Calls the `run_experiment()` function for each executor configuration
     
2. Transfer trace folders from RPi to laptop with the [`retrieve_traces.bash`](https://github.com/RaduLucianR/ros2-latency-analysis/blob/main/scripts/retrieve_traces.bash) script from the `scripts` folder:
   ```
   ./retrieve_traces.bash -i <IP_address_of_the_Raspberry> -u <raspberry_username> -p <raspberry_password> -f <which_trace_folder_to_process: latest|all>
   ```
   
3. Create CARET architecture files for all trace folders with the [`retrieve_traces.bash`](https://github.com/RaduLucianR/ros2-latency-analysis/blob/main/scripts/make-archi-files.bash) script from the `scripts` folder:
   ```
   ./make-archi-files.bash <folder_with_trace_folders>
   ```
   
4. Add the path from the ROS2 graph that you want to analyze (i.e. for which you want to find the end-to-end latency), to the architecture file. The path must be given a name, and it is defined by providing its start and end nodes. Add this path to all trace folders with the [`add-path-archi.py`](https://github.com/RaduLucianR/ros2-latency-analysis/blob/main/process/add-path-archi.py) script from the `process` folder:
   ```
   python3 add-path-archi.py /path/to/folder/with/trace/folders <start_node_of_ros2_path> <end_node_of_ros2_path> <desired_name_for_ros2_path> --subfolders True
   ```
5. Generate end-to-end latencies and .csv with all the latency data from the trace as byproducts of generating plots for each trace folder. Do this with the [`get-plots.py`](https://github.com/RaduLucianR/ros2-latency-analysis/blob/main/process/get-plots.py) script from the `process` folder:
   ```
   python3 get-plots.py /path/to/folder/with/trace/folders <given_name_of_ros2_path> /path/to/folder/where/to/store/the/plots --subfolders True
   ```
6. Use a script to iterate over all trace folders, read the data for each trace folder, and plot them in the same plot. For instance, you can use the [`t2-10-all-plots.py`](https://github.com/RaduLucianR/ros2-latency-analysis/blob/main/plot/t2-10-all-plots.py) script from `plot` folder:
   ```
   python3 t2-10-all-plots.py
   ```
   One has to modify the `t2-10-all-plots.py` script to use the correct path to the folder containing the trace folders.
