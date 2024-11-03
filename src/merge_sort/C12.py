"""
File: c12.py
Create Date: 2024-10-23
Description:
    - This script processes all groups (G0 to G9) using parallel merge sort.
    - It measures the time taken to process each group by varying the number of processes.
    - The results are presented in the required format for C12.
"""

import numpy as np
import os
import time
from utils import parallel_merge_sort
import multiprocessing

def process_all_groups_parallel(data_dir, n_processes):
    group_times = []
    group_cumulative_times = []
    total_cumulative_time = 0

    for group_index in range(10):  # G0 to G9
        print(f"Processing Group G{group_index}")
        group_dir = os.path.join(data_dir, f'G{group_index}')
        group_time = 0

        for array_index in range(8):  # A0 to A7
            print(f"Processing Array A{array_index}")
            array_filename = os.path.join(group_dir, f'A{array_index}.npy')
            Ai = np.load(array_filename)
            Ai_list = Ai.tolist()

            # Record the time before and after sorting
            start_time = time.time()

            # Create a pool with n_processes
            with multiprocessing.Pool(processes=n_processes) as pool:
                sorted_Ai = parallel_merge_sort(Ai_list, pool)

            end_time = time.time()

            # Calculate time taken to sort this array
            elapsed_time = end_time - start_time
            group_time += elapsed_time

        group_times.append(group_time)
        total_cumulative_time += group_time
        group_cumulative_times.append(total_cumulative_time)

    return group_times, group_cumulative_times

if __name__ == "__main__":
    # Define relative path to the data directory
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.join(current_dir, '..', '..', 'data')  # Path to the 'data' directory

    # Define number of processes to test
    process_counts = [1, 2, 4, 8]  # Adjust based on your CPU cores

    # Store results in a dictionary
    results = {}

    for n_processes in process_counts:
        print(f"\nRunning with {n_processes} processes:")
        group_times, group_cumulative_times = process_all_groups_parallel(data_dir, n_processes)
        results[n_processes] = {'group_times': group_times, 'cumulative': group_cumulative_times}

    # Print the results in the required format
    print("MergeSort - C12: Processing time of all groups under multiprocessing implementation")
    header = f"{' ':<10}" + "".join([f"{'Measured MP Time':<68}", f"{'Measured Cumulative MP Time':<68}"])
    subheader = f"{'GrpIndex':<10}" + "".join([f"{p:<17}" for p in process_counts] * 2)
    print(header)
    print(subheader)

    for i in range(10):
        row = f"{i:<10}"
        for p in process_counts:
            row += f"{results[p]['group_times'][i]:<17.12f}"
        for p in process_counts:
            row += f"{results[p]['cumulative'][i]:<17.12f}"
        print(row)
