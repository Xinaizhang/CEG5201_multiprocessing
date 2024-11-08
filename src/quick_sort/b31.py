import time
import numpy as np
import os


def load_arrays(group_dir):
    arrays = []
    for i in range(8):  # A0-A7 共8个文件
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

num_groups = 1
num_arrays = 8

log_file = 'sorting_times_b31.log'

total_time = 0

for group_num in range(num_groups):
    group_dir = f'../../data/G{group_num}'

    arrays = load_arrays(group_dir)

    group_time = 0
    group_message = f"Processing group {group_num}:"

    for i, A_i in enumerate(arrays):
        start_time = time.perf_counter()
        sorted_array = quicksort(A_i.tolist())
        end_time = time.perf_counter()
        time_taken = end_time - start_time
        group_time += time_taken
        group_message += f"\nArray A{i} sorted in {time_taken:.20f} seconds. Cumulative Sequential time in {group_time:.20f} seconds."

    total_time += group_time
    log_time(log_file, group_message)

group_message += f"\nOverall sequential sorting time for all groups: {total_time:.20f} seconds.\n\n"
log_time(log_file, group_message)
