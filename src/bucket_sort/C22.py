import numpy as np
import os
import time
from multiprocessing import Pool
from utils import prepare_buckets, sort_bucket

# Load the data
data_path = '../../data'
groups = [[np.load(os.path.join(data_path, f'G{g}', file), allow_pickle=True)
           for file in os.listdir(os.path.join(data_path, f'G{g}')) if file.endswith('.npy')]
          for g in range(10)]

# Parallel processing
def measure_mp_time_for_group(group, num_processes, N=10):
    group_start_time = time.time()
    for array in group:
        buckets = prepare_buckets(array, N)
        with Pool(processes=num_processes) as pool:
            pool.map(sort_bucket, buckets)
    group_end_time = time.time()
    return group_end_time - group_start_time

if __name__ == '__main__':
    process_counts = [1, 2, 4, 8]
    
    group_times_table = {p: [] for p in process_counts}
    cumulative_times_table = {p: [] for p in process_counts}
    
    for p in process_counts:
        cumulative_time = 0
        print(f"\nProcesses: {p}")
        print("Group Index\tMP Time (s)\tCumulative MP Time (s)")
        for g, group in enumerate(groups):
            group_time = measure_mp_time_for_group(group, p)
            cumulative_time += group_time
            group_times_table[p].append(group_time)
            cumulative_times_table[p].append(cumulative_time)
            print(f"{g}\t\t{group_time:.6f}\t\t{cumulative_time:.6f}")