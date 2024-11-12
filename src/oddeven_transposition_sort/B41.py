import numpy as np
import os
import time
import csv
from utils import odd_even_sort

def process_group_sequential(group_dir):
    sequential_times = []
    cumulative_times = []
    
    cumulative_time = 0
    
    for array_index in range(8):
        array_filename = os.path.join(group_dir, f'A{array_index}.npy')
        Ai = np.load(array_filename)
        Ai_list = Ai.tolist()

        start_time = time.time()
        sorted_Ai = odd_even_sort(Ai_list)
        end_time = time.time()

        elapsed_time = end_time - start_time
        sequential_times.append(elapsed_time)
        
        cumulative_time += elapsed_time
        cumulative_times.append(cumulative_time)
    # sequential_times: The sorting time of each array.
    # cumulative_times: The cumulative sorting time of each array.
    return sequential_times, cumulative_times

if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.join(current_dir, '..', '..', 'data', 'G0')

    sequential_times, cumulative_times = process_group_sequential(data_dir)

    print('Odd-Even Transposition Sort - B41: Processing time of G0 under sequential implementation')
    print(f"{'Array Ai':<14}{'Measured Sequential Time':<30}{'Cumulative Sequential Time'}")
    for i in range(8):
        print(f"{i:<14}{sequential_times[i]:<30.13f}{cumulative_times[i]:.13f}")

    output_file = os.path.join(current_dir, 'data', 'B41.csv')
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(sequential_times)
        writer.writerow(cumulative_times)
    
    print(f"Data saved to {output_file}")