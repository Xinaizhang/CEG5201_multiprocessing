import numpy as np
import os
import time
import random
# from utils import parallel_odd_even_sort
import multiprocessing

def compare_and_swap(shared_list, i):
    # 直接在共享列表上操作
    if shared_list[i] > shared_list[i + 1]:
        shared_list[i], shared_list[i + 1] = shared_list[i + 1], shared_list[i]

def parallel_odd_even_sort(arr, num_processes):
    n = len(arr)
    sorted = False

    # 使用 Manager 创建一个共享列表
    with multiprocessing.Manager() as manager:
        shared_list = manager.list(arr)

        # 手动设置进程池的大小
        with multiprocessing.Pool(processes=num_processes) as pool:
            while not sorted:
                sorted = True

                # 奇数阶段
                odd_indices = [(shared_list, i) for i in range(1, n - 1, 2)]
                pool.starmap(compare_and_swap, odd_indices)
                # 偶数阶段
                even_indices = [(shared_list, i) for i in range(0, n - 1, 2)]
                pool.starmap(compare_and_swap, even_indices)

                # 检查是否已排序
                sorted = all(shared_list[i] <= shared_list[i + 1] for i in range(n - 1))

        return list(shared_list)


def process_group_parallel(group_dir, n_processes):
    times = []
    cumulative_times = []
    cumulative_time = 0

    for array_index in range(8):  # A0 to A7
        print(f"Processing Array A{array_index}")
        array_filename = os.path.join(group_dir, f'A{array_index}.npy')
        Ai = np.load(array_filename)  # Load array from file
        Ai_list = Ai.tolist()  # Convert numpy array to list
        # Ai_list = Ai
        print(len(Ai_list))
        data = [random.randint(1, 255) for _ in range(200)]
        # Record the time before and after sorting
        start_time = time.time()

        sorted_Ai = parallel_odd_even_sort(data, n_processes)
        
        end_time = time.time()
        print(end_time-start_time)

        # Calculate time taken to sort this array
        elapsed_time = end_time - start_time
        times.append(elapsed_time)

        # Update cumulative time
        cumulative_time += elapsed_time
        cumulative_times.append(cumulative_time)

    return times, cumulative_times

if __name__ == "__main__":
    # Define relative path to the data directory
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.join(current_dir, '..', '..', 'data', 'G0')  # Path to group G0

    # Define number of processes to test
    process_counts = [1, 2, 4, 8]  # Adjust based on your CPU cores

    # Store results in a dictionary
    results = {}

    for n_processes in process_counts:
        print(f"\nRunning with {n_processes} processes:")
        times, cumulative_times = process_group_parallel(data_dir, n_processes)
        results[n_processes] = {'times': times, 'cumulative': cumulative_times}

    # Print the results in the required format
    print("Odd-Even Transposition Sort - C11: Processing time of G0 under multiprocessing implementation")
    header = f"{' ':<10}" + "".join([f"{'Measured MP Time':<68}", f"{'Measured Cumulative MP Time':<68}"])
    subheader = f"{'PairIndex':<10}" + "".join([f"{p:<17}" for p in process_counts] * 2)
    print(header)
    print(subheader)

    for i in range(8):
        row = f"{i:<10}"
        for p in process_counts:
            row += f"{results[p]['times'][i]:<17.12f}"
        for p in process_counts:
            row += f"{results[p]['cumulative'][i]:<17.12f}"
        print(row)
