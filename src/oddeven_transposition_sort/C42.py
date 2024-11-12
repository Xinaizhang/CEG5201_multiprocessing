import numpy as np
import os
import time
from utils import parallel_odd_even_sort
import csv
import random
import ctypes
import multiprocessing
from multiprocessing import Pool


def process_all_groups_parallel(data_dir, n_processes):
    group_times = []
    group_cumulative_times = []
    total_cumulative_time = 0

    for group_index in range(10):
        print(f"Processing Group G{group_index}")
        group_dir = os.path.join(data_dir, f'G{group_index}')
        group_time = 0

        for array_index in range(8):
            print(f"Processing Array A{array_index}")
            array_filename = os.path.join(group_dir, f'A{array_index}.npy')
            Ai = np.load(array_filename)
            Ai_list = Ai.tolist()

            start_time = time.time()

            sorted_Ai = parallel_odd_even_sort(Ai_list, n_processes)

            end_time = time.time()

            elapsed_time = end_time - start_time
            group_time += elapsed_time

        group_times.append(group_time)
        total_cumulative_time += group_time
        group_cumulative_times.append(total_cumulative_time)
    # group_times: The sorting time of each group in Multi-process.
    # group_cumulative_times: The cumulative sorting time of each group in Multi-process.
    return group_times, group_cumulative_times

if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.join(current_dir, '..', '..', 'data') 

    process_counts = [1, 2, 4, 8]
    results = {}

    for n_processes in process_counts:
        print(f"\nRunning with {n_processes} processes:")
        group_times, group_cumulative_times = process_all_groups_parallel(data_dir, n_processes)
        results[n_processes] = {'group_times': group_times, 'cumulative': group_cumulative_times}

    print("Odd-Even Transposition Sort - C42: Processing time of all groups under multiprocessing implementation")
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

    output_file = os.path.join(current_dir, 'data', 'C42.csv')
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for p in process_counts:
            writer.writerow(results[p]['group_times'])
        for p in process_counts:
            writer.writerow(results[p]['cumulative'])
    
    print(f"Data saved to {output_file}")