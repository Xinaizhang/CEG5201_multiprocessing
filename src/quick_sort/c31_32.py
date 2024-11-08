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


def partition_data(arr, pivot):
    low = [x for x in arr if x <= pivot]
    high = [x for x in arr if x > pivot]
    return low, high


def parallel_quicksort(arr, n_processes):
    if len(arr) <= 1:
        return arr

    with Manager() as manager:
        shared_arr = manager.list(arr)

        depth = 0
        with Pool(processes=n_processes) as pool:
            while depth < n_processes and len(shared_arr) > 1:
                pivot = random.choice(shared_arr)

                results = pool.starmap(partition_data,
                                       [(shared_arr[i::n_processes], pivot) for i in range(n_processes)])

                low, high = [], []
                for low_part, high_part in results:
                    low.extend(low_part)
                    high.extend(high_part)

                if depth < n_processes // 2:
                    shared_arr[:] = low
                else:
                    shared_arr[:] = high
                depth += 1

            sorted_sublists = pool.map(quicksort, [shared_arr[i::n_processes] for i in range(n_processes)])
            result = []
            for sublist in sorted_sublists:
                result.extend(sublist)
            return result


if __name__ == '__main__':
    num_groups = 10
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
                start_time = time.perf_counter()
                sorted_array = parallel_quicksort(A_i, processor)
                end_time = time.perf_counter()

                time_taken = end_time - start_time
                group_time += time_taken
                array_cul_time += time_taken
                group_cul_time += time_taken
                array_message += f"\n{time_taken:.20f}"
                group_message += f"\n{array_cul_time:.20f}"
            group_message += f"\ngroup{group_num} done takes {group_time:.20f}\n "
            group_cul_message += f"group done cultimate time takes {group_cul_time:.20f}\n"
            log_time(log_file, array_message)
            log_time(log_file, group_message)
        log_time(log_file, group_cul_message)
