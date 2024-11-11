"""
File: c11_v1.py
Create Date: 2024-10-23
Description:
    - This script processes group G0 using merge sort with parallel processing.
    - It measures the time taken to process each array and the cumulative time.
    - The results are presented in the required format for C11.
"""

import numpy as np
import os
import time
from utils import merge_sort, merge
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

        # Split the array into chunks
        num_chunks = n_processes
        chunk_size = len(Ai_list) // num_chunks
        chunks = [Ai_list[i*chunk_size : (i+1)*chunk_size] for i in range(num_chunks)]
        # Handle remaining elements
        if len(Ai_list) % num_chunks != 0:
            chunks[-1].extend(Ai_list[num_chunks*chunk_size:])

        start_time = time.time()
        
        with multiprocessing.Pool(processes=n_processes) as pool:
            # Sort each chunk in parallel
            sorted_chunks = pool.map(merge_sort, chunks)

        # Merge the sorted chunks iteratively
        while len(sorted_chunks) > 1:
            merged_chunks = []
            for i in range(0, len(sorted_chunks), 2):
                if i + 1 < len(sorted_chunks):
                    merged = merge(sorted_chunks[i], sorted_chunks[i+1])
                else:
                    merged = sorted_chunks[i]
                merged_chunks.append(merged)
            sorted_chunks = merged_chunks

        sorted_Ai = sorted_chunks[0] if sorted_chunks else []

        end_time = time.time()

        elapsed_time = end_time - start_time
        times.append(elapsed_time)

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
