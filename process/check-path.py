import os
import yaml

def aaa(path):
    for item in os.listdir(path):
        if not item.endswith(".yaml"):
            continue
        
        with open(f"{path}/{item}", 'r') as file:
            data = yaml.safe_load(file)

            if len(data["named_paths"]) != 0:
                print(item)
    
print(aaa("/home/lucian/tracing"))
