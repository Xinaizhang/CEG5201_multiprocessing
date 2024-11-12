import numpy as np
import os
import time
from B41 import process_group_sequential

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

if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.join(current_dir, '..', '..', 'data')

    group_times, cumulative_times = process_all_groups_sequential(data_dir)

    print('Odd-Even Transposition Sort - B42: Processing time of all groups under sequential implementation')
    print(f"{'Group Index':<14}{'Sequential Time (Group)':<25}{'Cumulative Sequential Time (Group)'}")
    for i in range(10):
        print(f"{i:<14}{group_times[i]:<25.13f}{cumulative_times[i]:.13f}")
