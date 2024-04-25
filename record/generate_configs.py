import math
import argparse

def nrof_execs(nrof_tasks : int):
    if nrof_tasks <= 1:
        raise ValueError("The number of tasks must be at least 2!")

    execs = set()
    execs.add(1)
    execs.add(nrof_tasks)

    if nrof_tasks <= 5:
        execs.add(math.ceil(nrof_tasks / 2))
    else:
        if nrof_tasks % 2 == 0:
            half = nrof_tasks // 2
            q1 = (1 + half) // 2
            q3 = (half + nrof_tasks) // 2

            execs.add(half)

        if nrof_tasks % 2 == 1:
            half = nrof_tasks / 2
            q1 = int(math.ceil((1 + half) / 2))
            q3 = int((half + nrof_tasks) // 2)

            if nrof_tasks > 14:
                execs.add(math.ceil(half))

        execs.add(q1)
        execs.add(q3)

    return sorted(execs)

def majority_executor(ttoe : str):
    if ttoe.count("1") > len(ttoe) // 2 - 1:
        return True

    return False


def exec_types(nrof_execs : int, ttoe : str):
    types = set()
    types_list = ["s" * nrof_execs, 
             "m" * nrof_execs,
             "s" * math.ceil(nrof_execs / 2) + "m" * math.floor(nrof_execs / 2),
             "m" * math.ceil(nrof_execs / 2) + "s" * math.floor(nrof_execs / 2)
    ]

    for t in types_list:
        types.add(t)

    return sorted(types)

def t2e(nrof_tasks : int, nrof_execs : int):
    if nrof_execs > nrof_tasks:
        raise ValueError("The number of executors can't be larger than the number of tasks!")
    
    task_to_exec = set()

    # Distribute tasks as evenly as possible to the executors
    t2e_ratio = nrof_tasks // nrof_execs
    t2e_rem = nrof_tasks % nrof_execs
    
    task_to_exec.add(
        "".join([str(x) * (t2e_ratio + 1) for x in range(1, t2e_rem  + 1)]
              + [str(x) * t2e_ratio for x in range(t2e_rem  + 1, nrof_execs  + 1)]
        )
    )

    # One executor has the majority of the tasks, rest of the executors have only one task
    task_to_exec.add(
        "1" * (nrof_tasks - (nrof_execs - 1)) + "".join([str(x) for x in range(2, nrof_execs + 1)])
    )

    return sorted(task_to_exec)

def e2c(nrof_execs : int, ttoe : str):
    nrof_cores = 4
    cores = set()

    all_one = "0-" * nrof_execs
    all_one = all_one[0:-1]
    cores.add(all_one)

    e2c_ratio = nrof_execs // nrof_cores
    e2c_rem = nrof_execs % nrof_cores
    distribute_cores = "".join([(str(x) + "-") * (e2c_ratio + 1) for x in range(0, e2c_rem)]
                            +  [(str(x) + "-") * e2c_ratio for x in range(e2c_rem, nrof_cores)]
        )
    cores.add(distribute_cores[0:-1])

    if nrof_execs >= 4:
        half_cores = ""

        if nrof_execs % 2 == 0:
            half_cores = "0-" * (nrof_execs // 2)
            half_cores += "1-" * (nrof_execs // 2)
        else:
            half_cores = "0-" * ((nrof_execs + 1) // 2)
            half_cores += "1-" * ((nrof_execs - 1) // 2)
        
        half_cores = half_cores[0:-1]
        cores.add(half_cores)

    return cores

def main(min_nrof_tasks : int, max_nrof_tasks : int):
    configs = set()

    for nrof_tasks in range(min_nrof_tasks, max_nrof_tasks + 1):
        nrofexecs = nrof_execs(nrof_tasks)
        
        for e in nrofexecs:
            t = nrof_tasks
            ttoe = t2e(t, e)
            sm = exec_types(e)
            etoc = e2c(e)

            # print(ttoe, majority_executor(ttoe))
            # if majority_executor(ttoe):
            #     c = "0-" + "1-" * (nrof_execs - 1)
            #     c = c[0:-1]
            #     etoc.add(c)

            # if majority_executor(ttoe):
            #     s = "s" + "m" * (nrof_execs - 1)
            #     types.add(s)
            #     s = "m" + "s" * (nrof_execs - 1)
            #     types.add(s)

            for seq in sm:
                for te in ttoe:
                    for ec in etoc:
                        configs.add(f"t{t}e{e}_{seq}_{te}_{ec}")
    
    print(*sorted(configs), sep='\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Executor Architecture names.")
    parser.add_argument("min_nrof_nodes", type=int, help="Minimum number of tasks in the node chain.")
    parser.add_argument("max_nrof_nodes", type=int, help="Maximum number of tasks in the node chain.")

    args = parser.parse_args()

    main(args.min_nrof_nodes, args.max_nrof_nodes)
