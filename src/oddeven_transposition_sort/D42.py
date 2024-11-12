import csv
import os
import numpy as np
import matplotlib.pyplot as plt


current_dir = os.path.dirname(__file__)
data_file1 = os.path.join(current_dir, 'data', 'B42.csv')
    
with open(data_file1, 'r') as csvfile:
        reader = csv.reader(csvfile)
        sequential_time = next(reader) 
        cumulative_time = next(reader) 

sequential_time = np.array([round(float(value), 6) for value in sequential_time])
cumulative_time = np.array([round(float(value), 6) for value in cumulative_time])


data_file2 = os.path.join(current_dir, 'data', 'C42.csv')
    
with open(data_file2, 'r') as csvfile:
        reader = csv.reader(csvfile)
        parallel_time1 = next(reader) 
        parallel_time2 = next(reader) 
        parallel_time3 = next(reader) 
        parallel_time4 = next(reader) 
        cumulative_time1 = next(reader) 
        cumulative_time2 = next(reader) 
        cumulative_time3 = next(reader) 
        cumulative_time4 = next(reader) 

array_indices = np.arange(10)

parallel_times = {
    1: np.array([round(float(value), 6) for value in parallel_time1]),
    2: np.array([round(float(value), 6) for value in parallel_time2]),
    4: np.array([round(float(value), 6) for value in parallel_time3]),
    8: np.array([round(float(value), 6) for value in parallel_time4])
}

speed_ups = {p: sequential_time / parallel_times[p] for p in parallel_times}

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

for process_count in parallel_times.keys():
    axes[0].plot(array_indices, speed_ups[process_count], marker='o', label=f'Processes={process_count}')

axes[0].set_title("Measured Speed-Up with Different Processor Numbers (D42)")
axes[0].set_xlabel("Group Index")
axes[0].set_ylabel("Measured Speed-Up")
axes[0].legend()
axes[0].grid(True)

for process_count in parallel_times.keys():
    cumulative_speed_up = [
        np.sum(sequential_time[:i+1]) / np.sum(parallel_times[process_count][:i+1])
        for i in range(len(array_indices))
    ]
    axes[1].plot(array_indices, cumulative_speed_up, marker='o', label=f'Processes={process_count}')

axes[1].set_title("Cumulative Speed-Up with Different Processor Numbers (D42)")
axes[1].set_xlabel("Group Index")
axes[1].set_ylabel("Cumulative Speed-Up")
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.show()
