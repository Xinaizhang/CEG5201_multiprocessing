"""
File: B11.py
Create Date: 2024-10-23
Description:
    - This script processes the arrays in group G0 sequentially using merge sort.
    - It measures the time taken to sort each array and the cumulative time.
    - The results are presented in the required format.
"""
import numpy as np
import os
import time
from utils import merge_sort

# B11 - Load and process each group sequentially
def process_group_sequential(group_dir):
    sequential_times = []
    cumulative_times = []
    
    cumulative_time = 0  # Initialize cumulative_time
    
    for array_index in range(8):  # A0 to A7
        array_filename = os.path.join(group_dir, f'A{array_index}.npy')
        Ai = np.load(array_filename)  # Load array from file
        
        # Record the time before and after sorting
        start_time = time.time()
        sorted_Ai = merge_sort(Ai)  # Sort the array using merge sort
        end_time = time.time()
        
        # Calculate time taken to sort this array
        elapsed_time = end_time - start_time
        sequential_times.append(elapsed_time)
        
        # Update cumulative time correctly
        cumulative_time += elapsed_time
        cumulative_times.append(cumulative_time)  # Append to the list
    
    return sequential_times, cumulative_times

if __name__ == "__main__":
    # Define relative path to the data directory
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.join(current_dir, '..', '..', 'data', 'G0')  # Path to group G0

    # Process the G0 group
    sequential_times, cumulative_times = process_group_sequential(data_dir)

    # Present results in the required format
    print('MergeSort - B11: Processing time of G0 under sequential implementation')
    print(f"{'Array Ai':<14}{'Measured Sequential Time':<30}{'Cumulative Sequential Time'}")
    for i in range(8):
        print(f"{i:<14}{sequential_times[i]:<30.13f}{cumulative_times[i]:.13f}")
