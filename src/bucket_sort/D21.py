import numpy as np
import time
import matplotlib.pyplot as plt
from multiprocessing import Pool
from utils import sequential_bucket_sort, parallel_bucket_sort

# Load data G0
G0 = [np.load(f'../../data/G0/A{i}.npy') for i in range(8)]

def measure_speedup_G0():
    sequential_times = []
    multiprocessing_times = {p: [] for p in [1, 2, 4, 8]}

    # Calculate sequential time
    for arr in G0:
        start = time.time()
        sequential_bucket_sort(arr)
        sequential_times.append(time.time() - start)

    # Calculate parallel time
    for p in [1, 2, 4, 8]:
        for arr in G0:
            start = time.time()
            parallel_bucket_sort(arr, p)
            multiprocessing_times[p].append(time.time() - start)

    # Calculate speedup
    speedups = {p: [] for p in [1, 2, 4, 8]}
    for p in [1, 2, 4, 8]:
        for seq_time, mp_time in zip(sequential_times, multiprocessing_times[p]):
            speedups[p].append(seq_time / mp_time)


    plt.figure(figsize=(10, 5))
    for p in [1, 2, 4, 8]:
        plt.plot(range(len(G0)), speedups[p], marker='o', label=f'Processes={p}')
    plt.xlabel("Array Index in G0")
    plt.ylabel("Measured Speed-Up")
    plt.title("Measured Speed-Up with Different Processor Numbers (D21)")
    plt.legend()
    plt.grid()
    plt.show()

    cumulative_speedups = {p: [] for p in [1, 2, 4, 8]}
    for p in [1, 2, 4, 8]:
        cumulative_seq_time = 0
        cumulative_mp_time = 0
        for i in range(len(G0)):
            cumulative_seq_time += sequential_times[i]
            cumulative_mp_time += multiprocessing_times[p][i]
            cumulative_speedups[p].append(cumulative_seq_time / cumulative_mp_time)

    plt.figure(figsize=(10, 5))
    for p in [1, 2, 4, 8]:
        plt.plot(range(len(G0)), cumulative_speedups[p], marker='o', label=f'Processes={p}')
    plt.xlabel("Array Index in G0")
    plt.ylabel("Cumulative Speed-Up")
    plt.title("Cumulative Speed-Up with Different Processor Numbers (D21)")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    measure_speedup_G0()