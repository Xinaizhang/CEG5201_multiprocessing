import numpy as np
import os
import time
from utils import parallel_odd_even_sort
import csv
import random
import ctypes
import multiprocessing
from multiprocessing import Pool


def process_group_parallel(group_dir, n_processes):
    times = []
    cumulative_times = []
    cumulative_time = 0

    for array_index in range(8):
        print(f"Processing Array A{array_index}")
        array_filename = os.path.join(group_dir, f'A{array_index}.npy')
        Ai = np.load(array_filename)
        Ai_list = Ai.tolist() 
        # print(len(Ai_list))
        start_time = time.time()

        sorted_Ai = parallel_odd_even_sort(Ai_list, n_processes)
        
        end_time = time.time()
        # print(end_time-start_time)

        elapsed_time = end_time - start_time
        times.append(elapsed_time)

        cumulative_time += elapsed_time
        cumulative_times.append(cumulative_time)
    # times: The sorting time of each array in Multi-process.
    # cumulative_times: The cumulative sorting time of each array in Multi-process.
    return times, cumulative_times

if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.join(current_dir, '..', '..', 'data', 'G0') 

    process_counts = [1, 2, 4, 8] 

    results = {}

    for n_processes in process_counts:
        print(f"\nRunning with {n_processes} processes:")
        times, cumulative_times = process_group_parallel(data_dir, n_processes)
        results[n_processes] = {'times': times, 'cumulative': cumulative_times}

    print("Odd-Even Transposition Sort - C41: Processing time of G0 under multiprocessing implementation")
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

    output_file = os.path.join(current_dir, 'data', 'C41.csv')
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for p in process_counts:
            writer.writerow(results[p]['times'])
        for p in process_counts:
            writer.writerow(results[p]['cumulative'])
    
    print(f"Data saved to {output_file}")