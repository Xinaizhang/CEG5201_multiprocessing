import numpy as np
import os
import time
import matplotlib.pyplot as plt
from multiprocessing import Pool
from utils import sequential_bucket_sort, parallel_bucket_sort

# Load data
data_path = '../../data'
groups = [[np.load(os.path.join(data_path, f'G{g}', file), allow_pickle=True)
           for file in os.listdir(os.path.join(data_path, f'G{g}')) if file.endswith('.npy')]
          for g in range(10)]

def measure_speedup_all_groups():
    process_counts = [1, 2, 4, 8]
    measured_speedups = {p: [] for p in process_counts}
    cumulative_speedups = {p: [] for p in process_counts}

    for g, group in enumerate(groups):
        # Calculate sequential processing time
        sequential_times = []
        for arr in group:
            start = time.time()
            sequential_bucket_sort(arr)
            sequential_times.append(time.time() - start)

        # 计算多进程时间和加速比
        for p in process_counts:
            multiprocessing_times = []
            for arr in group:
                start = time.time()
                parallel_bucket_sort(arr, p)
                multiprocessing_times.append(time.time() - start)

            # Calculate speedup
            speedups = [seq_time / mp_time for seq_time, mp_time in zip(sequential_times, multiprocessing_times)]
            measured_speedups[p].append(sum(speedups) / len(speedups))  # 平均加速比

            cumulative_seq_time = sum(sequential_times)
            cumulative_mp_time = sum(multiprocessing_times)
            cumulative_speedups[p].append(cumulative_seq_time / cumulative_mp_time)

    # Plot the figure
    plt.figure(figsize=(10, 5))
    for p in [1, 2, 4, 8]:
        plt.plot(range(len(groups)), measured_speedups[p], marker='o', label=f'Processes={p}')
    plt.xlabel("Group Index")
    plt.ylabel("Measured Speed-Up")
    plt.title("Measured Speed-Up with Different Processor Numbers (D22)")
    plt.legend()
    plt.grid()
    plt.show()

    plt.figure(figsize=(10, 5))
    for p in [1, 2, 4, 8]:
        plt.plot(range(len(groups)), cumulative_speedups[p], marker='o', label=f'Processes={p}')
    plt.xlabel("Group Index")
    plt.ylabel("Cumulative Speed-Up")
    plt.title("Cumulative Speed-Up with Different Processor Numbers (D22)")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    measure_speedup_all_groups()