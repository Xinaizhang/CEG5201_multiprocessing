"""
File: B12.py
Create Date: 2024-10-23
Description:
    - This script processes all 10 groups (G0 to G9) sequentially using merge sort.
    - It measures the total time taken to process each group and the cumulative time.
    - The results are presented in the required format for Bn2 and saved to a CSV file.
"""
import numpy as np
import os
import time
import csv
from B11 import process_group_sequential

def process_all_groups_sequential(data_dir):
    group_times = []
    group_cumulative_times = []
    
    group_cumulative_time = 0
    
    for group_index in range(10):
        group_dir = os.path.join(data_dir, f'G{group_index}')
        
        print(f'Processing group G{group_index}...')
        
        sequential_times, cumulative_times = process_group_sequential(group_dir)
        group_time = cumulative_times[-1] 
        
        group_times.append(group_time)
        
        group_cumulative_time += group_time
        group_cumulative_times.append(group_cumulative_time)
    
    return group_times, group_cumulative_times

def save_group_results_to_csv(filename, group_times, group_cumulative_times):
    """Save the group processing times to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Group Index", "Sequential Time (Group)", "Cumulative Sequential Time (Group)"])
        for i in range(len(group_times)):
            writer.writerow([f"G{i}", f"{group_times[i]:.13f}", f"{group_cumulative_times[i]:.13f}"])

if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.join(current_dir, '..', '..', 'data')  # Path to the 'data' directory

    group_times, cumulative_times = process_all_groups_sequential(data_dir)

    print('MergeSort - B12: Processing time of all groups under sequential implementation')
    print(f"{'Group Index':<14}{'Sequential Time (Group)':<25}{'Cumulative Sequential Time (Group)'}")
    for i in range(10):
        print(f"{i:<14}{group_times[i]:<25.13f}{cumulative_times[i]:.13f}")
    
    output_filename = os.path.join(current_dir, 'B12_all_groups_processing_times.csv')
    save_group_results_to_csv(output_filename, group_times, cumulative_times)
    print(f"Results saved to {output_filename}")