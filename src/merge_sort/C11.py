"""
File: c11.py
Create Date: 2024-10-23
Description:
    - This script processes the arrays in group G0 using parallel merge sort.
    - It measures the time taken to sort each array by varying the number of processes.
    - The results are presented in the required format for C11.
"""

import numpy as np
import os
import time
from utils import parallel_merge_sort
import multiprocessing

def process_group_parallel(group_dir, n_processes):
    times = []
    cumulative_times = []
    cumulative_time = 0

    for array_index in range(8):  # A0 to A7
        print(f"Processing Array A{array_index}")
        array_filename = os.path.join(group_dir, f'A{array_index}.npy')
        Ai = np.load(array_filename)  # Load array from file
        Ai_list = Ai.tolist()  # Convert numpy array to list

        # Record the time before and after sorting
        start_time = time.time()

        # Create a pool with n_processes
        with multiprocessing.Pool(processes=n_processes) as pool:
            sorted_Ai = parallel_merge_sort(Ai_list, pool)

        end_time = time.time()

        # Calculate time taken to sort this array
        elapsed_time = end_time - start_time
        times.append(elapsed_time)

        # Update cumulative time
        cumulative_time += elapsed_time
        cumulative_times.append(cumulative_time)

    return times, cumulative_times

if __name__ == "__main__":
    # Define relative path to the data directory
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.join(current_dir, '..', '..', 'data', 'G0')  # Path to group G0

    # Define number of processes to test
    process_counts = [1, 2, 4, 8]  # Adjust based on your CPU cores

    # Store results in a dictionary
    results = {}

    for n_processes in process_counts:
        print(f"\nRunning with {n_processes} processes:")
        times, cumulative_times = process_group_parallel(data_dir, n_processes)
        results[n_processes] = {'times': times, 'cumulative': cumulative_times}

    # Print the results in the required format
    print("MergeSort - C11: Processing time of G0 under multiprocessing implementation")
    header = f"{' ':<10}" + "".join([f"{'Measured MP Time':<68}", f"{'Measured Cumulative MP Time':<68}"])
    subheader = f"{'PairIndex':<10}" + "".join([f"{p:<17}" for p in process_counts] * 2)
    print(header)
    print(subheader)

    for i in range(8):
        row = f"{i:<10}"
        for p in process_counts:
            row += f"{results[p]['times'][i]:<17.12f}"
        for p in process_counts:
            row += f"{results[p]['cumulative'][i]:<17.12f}"
        print(row)
