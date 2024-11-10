# C12_v2.py

import numpy as np
import os
import time
import csv
import math
import multiprocessing
from utilsv2 import parallel_merge_sort, init_pool

def process_all_groups_parallel(data_dir, n_processes):
    group_times = []
    group_cumulative_times = []
    total_cumulative_time = 0

    # Calculate max_depth based on the number of processes
    max_depth = int(math.log2(n_processes)) if n_processes > 0 else 0

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

            # Create a pool with n_processes and initialize with max_depth
            with multiprocessing.Pool(processes=n_processes, initializer=init_pool, initargs=(None,)) as p:
                init_pool(p)  # Initialize the pool for use in parallel_merge_sort
                sorted_Ai = parallel_merge_sort(Ai_list, max_depth=max_depth)

            end_time = time.time()

            # Calculate time taken to sort this array and add to group time
            elapsed_time = end_time - start_time
            group_time += elapsed_time

        group_times.append(group_time)
        total_cumulative_time += group_time
        group_cumulative_times.append(total_cumulative_time)

    return group_times, group_cumulative_times

def save_results_to_csv(filename, results, process_counts):
    """Save the group processing results to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write headers for each process count
        header = ["GroupIndex"] + [f"Time_{p}P" for p in process_counts] + [f"Cumulative_{p}P" for p in process_counts]
        writer.writerow(header)

        # Write each row with group times and cumulative times for each process count
        for i in range(10):  # Assuming 10 groups (G0 to G9)
            row = [i]  # Start row with GroupIndex
            row.extend(results[p]['group_times'][i] for p in process_counts)  # Add group times for each process count
            row.extend(results[p]['cumulative'][i] for p in process_counts)  # Add cumulative times for each process count
            writer.writerow(row)

if __name__ == "__main__":
    multiprocessing.freeze_support()

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
    header = f"{' ':<10}" + "".join([f"{'Measured MP Time':<17}" for _ in process_counts]) + "".join([f"{'Measured Cumulative MP Time':<17}" for _ in process_counts])
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

    # Save results to CSV file
    output_filename = os.path.join(current_dir, 'C12_all_groups_parallel_processing_times.csv')
    save_results_to_csv(output_filename, results, process_counts)
    print(f"Results saved to {output_filename}")
