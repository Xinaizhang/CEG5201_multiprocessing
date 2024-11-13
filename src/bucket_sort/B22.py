import numpy as np
import os
import time
from utils import sequential_bucket_sort

# Load data
data_path = '../../data' 
groups = []
for i in range(10): # G0 to G9
    group_path = os.path.join(data_path, f'G{i}')
    arrays = []
    for j in range(8): # A0 to A7
        file_path = os.path.join(group_path, f'A{j}.npy')
        arrays.append(np.load(file_path, allow_pickle=True))
    groups.append(arrays)

# Sequential processing
group_times = []
cumulative_time = 0
for i, group in enumerate(groups):
    start_time = time.time()
    for arr in group:
        sorted_arr = sequential_bucket_sort(arr)
    end_time = time.time()
    elapsed_time = end_time - start_time
    cumulative_time += elapsed_time
    group_times.append((elapsed_time, cumulative_time))


# Output results
print("Sequential times and cumulative times for each group:")
for i, (time_single, time_cumulative) in enumerate(group_times):
    print(f"Group {i}: Time = {time_single:.6f} s, Cumulative Time = {time_cumulative:.6f} s")
