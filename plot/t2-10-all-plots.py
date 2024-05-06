import os
import re
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import math

which = ""

def extract_max_latency(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        match = re.search(r'max: ([\d.]+) ms', content)
        return float(match.group(1)), "Max" if match else None
    
def extract_avg_latency(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        match = re.search(r'avg: ([\d.]+) ms', content)
        return float(match.group(1)), "Avg" if match else None

def filtr(latency, payload):
    fact = 3

    # if 4000 * fact > payload or payload > 4000 * (fact + 1):
    #     return False

    if latency > 160:
        return False
    
    return True 
    
def check_config(tasks, execs, etypes, t2e, e2c):
    tasks = int(tasks)
    execs = int(execs)    
    stri = f"t{tasks}e{execs}_{etypes}_{t2e}_{e2c}"

    # if tasks == 3:
    # if tasks == 3 and execs == 3 and e2c == "1-1-1":
    # if stri in ["t3e2_ms_112_1-2"] or (tasks == 3 and execs == 3):
    # if stri in ["t3e2_ms_112_1-2", "t3e3_sss_123_1-1-1"]:
    # if tasks == 4 and execs == 2 and etypes == "ss" and e2c == "1-1":
    if tasks == 5:
    # if tasks == 6 and execs == 2 and e2c == "1-1":
    # if stri in ["t6e2_ms_111122_1-1", "t6e2_sm_111112_1-1", "t6e2_sm_111222_1-1"]:
    # if tasks == 7:
    # if tasks == 7 and all(char == 's' for char in etypes) and execs == 3:
    # if stri in [
    #     "t7e1_m_1111111_1",
    #     "t7e3_ssm_1111123_1-2-3",
    #     "t7e1_s_1111111_1",
    # ]:
    # if tasks == 8 and all(char == 's' for char in etypes):
    # if tasks == 8 and all(char == 's' for char in etypes) and execs <= 2:
    # if tasks == 8 and (execs == 1 or etypes == "ss"):
    # if tasks == 9 and (execs == 1 or etypes == "sss"):
    # if stri in ["t9e1_m_111111111_1", "t9e3_sss_111111123_1-2-2"]:
    # if stri in [
    #     "t9e2_ss_111111122_1-1",
    #     "t9e3_sss_111111123_1-2-2",
    #     "t9e1_s_111111111_1",
    #     "t9e2_ss_111112222_1-1",
    #     "t9e3_sss_111111123_1-2-3",
    #     "t9e1_m_111111111_1"
    # ]:
    # if tasks == 9 and execs != 9:
    # if stri in [
    #     "t7e2_sm_1111112_1-1",
    #     "t7e3_ssm_1111123_1-2-2",
    #     "t7e7_sssssss_1234567_0-1-1-2-2-3-3",
    #     "t7e7_mmmmmmm_1234567_0-1-1-2-2-3-3"
    # ]:
    # if tasks == 10:
    # if tasks == 10 and etypes != "mmm":
    # if tasks == 10 and etypes == "ssm":
    # if tasks == 10 and (execs == 1 or etypes == "ssm"):
    # if stri in ["t10e1_s_1111111111_1", "t10e3_mms_1111111123_1-1-1"]:
    # if stri in ["t10e3_ssm_1111111123_1-2-3", "t10e3_mms_1111111123_1-1-1"]:
    # if stri in [
    #     "t10e2_sm_1111122222_1-2",
    #     "t10e2_ss_1111111112_1-2",
    #     "t10e1_s_1111111111_1",
    #     "t10e2_ss_1111122222_1-2"
    # ]:
        return True
    
    return False

# Main function to process folders and plot data
def plot_lines(folder_path):
    same = False

    if folder_path == '/home/lucian/simple-chain-ws/graphs/two-ten-nodes-same-payload':
        same = True

    global which
    data = {}
    ct2 = 0

    for root, dirs, files in os.walk(folder_path):
        for dir_name in dirs:
            if same:
                match = re.match(r't(\d+)e(\d+)_([sm]+)_(\d+)_([\d-]+)_i(\d+)', dir_name)
            else:
                match = re.match(r't(\d+)e(\d+)_([sm]+)_(\d+)_([\d-]+)_(\d+\.\d+)KB', dir_name)

            if match:
                tasks, execs, etypes, t2e, e2c, payload = match.groups()

                if same:
                    payload_value = float(payload)
                else:
                    payload_value = float(payload[:-2])  # Convert payload size to float

                file_name = f"cl-e2e-{dir_name}"
                file_path = os.path.join(root, dir_name, file_name)

                if not os.path.isfile(file_path):
                    continue

                max_latency, which = extract_avg_latency(file_path)

                if max_latency is not None:
                    key = f"t{tasks}e{execs}_{etypes}_{t2e}_{e2c}"
                    
                    if key not in data.keys():
                        data[key] = []

                    if check_config(tasks, execs, etypes, t2e, e2c) and filtr(max_latency, payload_value):
                        data[key].append((payload_value, max_latency))

    plt.figure(figsize=(15, 6))
    np.random.seed(398157)  # For reproducibility
    num_categories = 10
    colors = plt.cm.tab10(np.linspace(0, 1, num_categories))
    ct = 0
    best = ["", math.inf, math.inf, math.inf, math.inf]

    for config in data:
        if data[config]:
            payloads, latencies = zip(*sorted(data[config]))

            values = latencies
            mean = round(stats.tmean(values), 4)
            variance = round(stats.tvar(values), 2)
            skewness = round(stats.skew(values), 2)
            kurtosis = round(stats.kurtosis(values), 2)
            print(f"{config} has M={mean}, V={variance}, S={skewness}, K={kurtosis}")
            
            if mean < best[1]:
                best[0] = config
                best[1] = mean
                best[2] = variance
                best[3] = skewness
                best[4] = kurtosis

            # payloads_array = np.array(payloads)
            # latencies_array = np.array(latencies)
            # slope, intercept = np.polyfit(payloads_array, latencies_array, 1)
            # trendline = slope * payloads_array + intercept
            # plt.plot(payloads_array, trendline, color=colors[ct], lw=3)  # Plotting the trend line

            plt.scatter(payloads, latencies, color=colors[ct], label=config)
            plt.plot(payloads, latencies, color=colors[ct])
            ct += 1
    
    # with open('top_configs_over_tasks.csv','a') as fd:
    #     fd.write(f"{best[0]}\n")
    
    # print("##########################################")
    print(f"Best is {best[0]} with M={best[1]}, V={best[2]}, S={best[3]}, K={best[4]}")

    ##### ANOVA
    latency_by_config = {config: np.array(sorted(data[config], key=lambda x: x[0]))[:, 1] for config in data if data[config]}

    if len(latency_by_config) == 2:
        anova_result = stats.f_oneway(*latency_by_config.values())
        print("ANOVA result:", anova_result)
        print("F-statistic:", anova_result.statistic)
        print("P-value:", anova_result.pvalue)
        if anova_result.pvalue < 0.05:
            print("There is a statistically significant difference between the configurations.")
        else:
            print("There is no statistically significant difference between the configurations.")

    ### Find the best with no statistically significant difference between them
    latency_by_config = {config: np.array(sorted(data[config], key=lambda x: x[0]))[:, 1] for config in data if data[config]}

    for c in latency_by_config.keys():
        if best[0] != c:
            anova_result = stats.f_oneway(latency_by_config[best[0]], latency_by_config[c])

            if anova_result.pvalue < 0.05:
                print(f"Significant difference between {best[0]} and {c}")
            else:
                print(f"No significant difference between {best[0]} and {c}")
                with open('top_configs_over_tasks.csv','a') as fd:
                    fd.write(f"{c}\n")
    
    # plt.title(f'{which} Latency vs Payload')
    # plt.xlabel('Payload (KB)')
    plt.title(f'{which} Latency vs Iteration')
    plt.xlabel('Iteration')

    plt.ylabel('Latency (ms)')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.subplots_adjust(right=0.75)
    plt.show()

plot_lines('/home/lucian/simple-chain-ws/graphs/two-ten-nodes-same-payload')
# plot_lines('/home/lucian/simple-chain-ws/graphs/two-ten-nodes-large-payload')
# plot_lines('/home/lucian/simple-chain-ws/graphs/two-ten-nodes-all')
# plot_lines('/home/lucian/simple-chain-ws/graphs/two-ten-nodes-best-configs')