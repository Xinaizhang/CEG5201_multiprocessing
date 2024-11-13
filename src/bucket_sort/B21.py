import numpy as np
import time
from utils import sequential_bucket_sort

# Load G0 data
G0 = [np.load(f'./data/G0/A{i}.npy') for i in range(8)]

# Sequential processing for G0
cumulative_time = 0
results = []
for i, arr in enumerate(G0):
    start_time = time.time()
    sequential_bucket_sort(arr)
    elapsed_time = time.time() - start_time
    cumulative_time += elapsed_time
    results.append((elapsed_time, cumulative_time))

# Output results
print("B21: Sequential Processing for G0")
for i, (time_single, time_cumulative) in enumerate(results):
    print(f"A{i}: Time = {time_single:.6f}s, Cumulative Time = {time_cumulative:.6f}s")