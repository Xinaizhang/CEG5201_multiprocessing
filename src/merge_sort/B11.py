"""
File: B11.py
Create Date: 2024-10-23
Description:
    - This script processes the arrays in group G0 sequentially using merge sort.
    - It measures the time taken to sort each array and the cumulative time.
    - The results are presented in the required format and saved to a CSV file.
"""
import numpy as np
import os
import time
import csv
from utils import merge_sort

def process_group_sequential(group_dir):
    sequential_times = []
    cumulative_times = []
    
    cumulative_time = 0
    
    for array_index in range(8):
        array_filename = os.path.join(group_dir, f'A{array_index}.npy')
        Ai = np.load(array_filename) 
        
        start_time = time.time()
        sorted_Ai = merge_sort(Ai) 
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        sequential_times.append(elapsed_time)
        
        cumulative_time += elapsed_time
        cumulative_times.append(cumulative_time)
    
    return sequential_times, cumulative_times

def save_results_to_csv(filename, sequential_times, cumulative_times):
    """Save the timing results to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Array Ai", "Measured Sequential Time", "Cumulative Sequential Time"])
        for i in range(len(sequential_times)):
            writer.writerow([f"A{i}", f"{sequential_times[i]:.13f}", f"{cumulative_times[i]:.13f}"])

if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.join(current_dir, '..', '..', 'data', 'G0')  # Path to group G0

    sequential_times, cumulative_times = process_group_sequential(data_dir)

    print('MergeSort - B11: Processing time of G0 under sequential implementation')
    print(f"{'Array Ai':<14}{'Measured Sequential Time':<30}{'Cumulative Sequential Time'}")
    for i in range(8):
        print(f"{i:<14}{sequential_times[i]:<30.13f}{cumulative_times[i]:.13f}")
    
    output_filename = os.path.join(current_dir, 'B11_G0_processing_times.csv')
    save_results_to_csv(output_filename, sequential_times, cumulative_times)
    print(f"Results saved to {output_filename}")
