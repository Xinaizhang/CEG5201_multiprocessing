import time
import os
import numpy as np

def load_arrays(group_dir):
    arrays = []
    for i in range(8):
        filename = f"{group_dir}/A{i}.npy"
        array = np.load(filename)
        arrays.append(array)
    return arrays

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)



def log_time(log_file, message):
    with open(log_file, 'a') as f:
        f.write(message + '\n')

num_groups = 10
num_arrays = 8

overall_total_time = 0
log_file = 'sorting_times_b32.log'

for group_num in range(num_groups):
    group_dir = f'../../data/G{group_num}'

    arrays = load_arrays(group_dir)

    print(f"\nProcessing group {group_num} from {group_dir}:")
    group_message = f"Processing group {group_num} from {group_dir}:"
    group_time = 0

    for array_idx, A_i in enumerate(arrays[:num_arrays]):
        start_time = time.perf_counter()
        sorted_array = quicksort(A_i)
        end_time = time.perf_counter()
        time_taken = end_time - start_time
        group_time += time_taken
        group_message += f"\nArray {array_idx + 1} sorted in {time_taken:.20f} seconds. Cumulative Sequential time in {group_time:.20f} seconds."

    overall_total_time += group_time
    group_message += f"\nTotal sequential sorting time for group {group_num}: {group_time:.20f} seconds."
    log_time(log_file, group_message)

group_message += f"\nOverall sequential sorting time for all groups: {overall_total_time:.20f} seconds.\n\n"
log_time(log_file, group_message)