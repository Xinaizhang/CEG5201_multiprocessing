"""
File: c11_v2.py
Create Date: 2024-10-30
Description:
    - This script processes group G0 using merge sort with parallel processing.
    - It measures the time taken to process each array and the cumulative time.
    - The results are presented in the required format for C11 and saved to a CSV file.
"""

import numpy as np
import os
import time
import csv
import math
import multiprocessing
from utilsv2 import parallel_merge_sort, init_pool

def process_group_parallel(group_dir, n_processes):
    times = []
    cumulative_times = []
    cumulative_time = 0


    max_depth = int(math.log2(n_processes)) if n_processes > 0 else 0

    for array_index in range(8):
        print(f"Processing Array A{array_index}")
        array_filename = os.path.join(group_dir, f'A{array_index}.npy')
        Ai = np.load(array_filename)
        Ai_list = Ai.tolist() 

        start_time = time.time()

        with multiprocessing.Pool(processes=n_processes, initializer=init_pool, initargs=(None,)) as p:
            init_pool(p)
            sorted_Ai = parallel_merge_sort(Ai_list, max_depth=max_depth)

        end_time = time.time()

        elapsed_time = end_time - start_time
        times.append(elapsed_time)

        cumulative_time += elapsed_time
        cumulative_times.append(cumulative_time)

    return times, cumulative_times

def save_results_to_csv(filename, results, process_counts):
    """Save the parallel processing results to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        header = ["PairIndex"] + [f"Time_{p}P" for p in process_counts] + [f"Cumulative_{p}P" for p in process_counts]
        writer.writerow(header)

        for i in range(8): 
            row = [i]
            row.extend(results[p]['times'][i] for p in process_counts)  # Add times for each process count
            row.extend(results[p]['cumulative'][i] for p in process_counts)  # Add cumulative times for each process count
            writer.writerow(row)

if __name__ == "__main__":
    multiprocessing.freeze_support()

    current_dir = os.path.dirname(__file__)
    data_dir = os.path.join(current_dir, '..', '..', 'data', 'G0')  # Path to group G0

    process_counts = [1, 2, 4, 8]

    results = {}

    for n_processes in process_counts:
        print(f"\nRunning with {n_processes} processes:")
        times, cumulative_times = process_group_parallel(data_dir, n_processes)
        results[n_processes] = {'times': times, 'cumulative': cumulative_times}

    print("MergeSort - C11: Processing time of G0 under multiprocessing implementation")
    header = f"{' ':<10}" + "".join([f"{'Measured MP Time':<17}" for _ in process_counts]) + "".join([f"{'Measured Cumulative MP Time':<17}" for _ in process_counts])
    subheader = f"{'PairIndex':<10}" + "".join([f"{p:<17}" for p in process_counts]*2)
    print(header)
    print(subheader)

    for i in range(8):
        row = f"{i:<10}"
        for p in process_counts:
            row += f"{results[p]['times'][i]:<17.12f}"
        for p in process_counts:
            row += f"{results[p]['cumulative'][i]:<17.12f}"
        print(row)

    output_filename = os.path.join(current_dir, 'C11_G0_parallel_processing_times.csv')
    save_results_to_csv(output_filename, results, process_counts)
    print(f"Results saved to {output_filename}")