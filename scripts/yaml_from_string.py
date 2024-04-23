import re

def yaml_from_string(config):
    regex = r"t(\d+)e(\d+)_([sm]+)_(\d+)_([\d-]+)"
    match = re.match(regex, config)
    yaml_exec_list = []

    if match:
        tasks, execs, etypes, t2e, e2c = match.groups()

        for e in range(1, int(execs) + 1):
            exec_type = ""

            # Executor type
            if etypes[e - 1] == "s":
                exec_type = "single_threaded"
            if etypes[e - 1] == "m":
                exec_type = "multi_threaded"

            # Core list
            cores_str = e2c.split("-")
            cores_list = [int(cores_str[e - 1])]

            # Node list
            node_list = []

            for i in range(0, int(tasks)):
                if str(e) == t2e[i]:
                    node = i + 1
                    node_name = f"node{node}"
                    subscribe = ""
                    publish = ""

                    if node != 1:
                        subscribe = f"topic{node - 1}"
                    else:
                        subscribe = f"NONE"
                    
                    if node != int(tasks):
                        publish = f"topic{node}"
                    else:
                        publish = "NONE"
                    
                    node_dict = {
                        "name" : node_name,
                        "subscribe" : subscribe,
                        "publish" : publish,
                        "payload" : "128B"
                    }

                    node_list.append(node_dict)

            # Make executor and add
            exec = {
                "name" : f"executor{e}",
                "type" : exec_type,
                "cores" : cores_list,
                "nodes" : node_list
            }

            yaml_exec_list.append(exec)

    return {"executors": yaml_exec_list}