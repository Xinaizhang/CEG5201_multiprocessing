import numpy as np
import os
import time
from multiprocessing import Pool
from utils import prepare_buckets, sort_bucket

# Load data G0
G0_path = './data/G0'
G0 = [np.load(os.path.join(G0_path, file), allow_pickle=True) for file in os.listdir(G0_path) if file.endswith('.npy')]

# Parallel processing
def measure_mp_time_for_array(array, num_processes, N=10):
    buckets = prepare_buckets(array, N)
    # Sort buckets in parallel
    start_time = time.time()
    with Pool(processes=num_processes) as pool:
        sorted_buckets = pool.map(sort_bucket, buckets)
    end_time = time.time()

    sorted_array = []
    for bucket in sorted_buckets:
        sorted_array.extend(bucket)
    return end_time - start_time

if __name__ == '__main__':
    process_counts = [1, 2, 4, 8]
    
    mp_times_table = {p: [] for p in process_counts}
    cumulative_times_table = {p: [] for p in process_counts}
    
    for array in G0:
        for p in process_counts:
            mp_time = measure_mp_time_for_array(array, p)
            mp_times_table[p].append(mp_time)
            
    # Calculate Measured Cumulative MP Time
    for p in process_counts:
        cumulative_time = 0
        for mp_time in mp_times_table[p]:
            cumulative_time += mp_time
            cumulative_times_table[p].append(cumulative_time)

    # Output the results
    print("Measured MP time and Measured Cumulative MP Time for each process count:")
    for p in process_counts:
        print(f"\nProcess count: {p}")
        print("Pair Index\tMP Time\t\tCumulative MP Time")
        for idx, (mp_time, cumulative_time) in enumerate(zip(mp_times_table[p], cumulative_times_table[p])):
            print(f"{idx}\t\t{mp_time:.6f}s\t{cumulative_time:.6f}s")

