import multiprocessing
import random
import time
from multiprocessing import Pool, Manager
import numpy as np


def load_arrays(group_dir):
    arrays = []
    for i in range(8):
        filename = f"{group_dir}/A{i}.npy"
        array = np.load(filename)
        arrays.append(array)
    return arrays


def log_time(log_file, message):
    with open(log_file, 'a') as f:
        f.write(message + '\n')


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr.pop(random.randint(0, len(arr) - 1))
    return quicksort([x for x in arr if x < pivot]) \
           + [pivot] \
           + quicksort([x for x in arr if x >= pivot])


def parallel_quicksort_task(arr):
    pivot = random.choice(arr)
    low_list = [x for x in arr if x <= pivot]
    high_list = [x for x in arr if x > pivot]
    return low_list, high_list

if __name__ == '__main__':
    num_groups = 10
    global pool
    log_file = 'sorting_times_c32.log'
    for processor in [1, 2, 4, 8]:
        group_cul_time = 0
        group_cul_message =f"\n"
        for group_num in range(num_groups):
            group_dir = f'../../data/G{group_num}'
            arrays = load_arrays(group_dir)
            array_message = f"Processing group {group_num} with processor {processor}:"
            group_message = f"Processing group {group_num} with processor {processor}:"
            array_cul_time = 0
            group_time = 0
            for i, A_i in enumerate(arrays):
                print(i)
                print(A_i)
                start_time = time.perf_counter()
                with multiprocessing.Pool(processes=processor) as pool:
                    tasks = [A_i]
                    sorted_sublists = []
                    while tasks:
                        new_tasks = []
                        async_results = [pool.apply_async(parallel_quicksort_task, (task,)) for task in tasks]
                        for result in async_results:
                            low_list, high_list = result.get()
                            if len(low_list) <= 100:
                                sorted_sublists.append(quicksort(low_list))
                            else:
                                new_tasks.append(low_list)

                            if len(high_list) <= 100:
                                sorted_sublists.append(quicksort(high_list))
                            else:
                                new_tasks.append(high_list)

                        tasks = new_tasks

                    sorted_data = [item for sublist in sorted_sublists for item in sublist]
                    sorted_data.sort()
                end_time = time.perf_counter()
                time_taken = end_time - start_time
                group_time += time_taken
                array_cul_time += time_taken
                group_cul_time += time_taken
                array_message += f"\n{time_taken:.20f}"
                group_message += f"\n{array_cul_time:.20f}"
                print(sorted_data)
            group_message += f"\ngroup{group_num} done takes {group_time:.20f}\n "
            group_cul_message += f"group done cultimate time takes {group_cul_time:.20f}\n"
            log_time(log_file, array_message)
            log_time(log_file, group_message)
        log_time(log_file, group_cul_message)
