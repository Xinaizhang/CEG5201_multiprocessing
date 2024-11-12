import numpy as np
import os
import time
# from utils import parallel_odd_even_sort
import multiprocessing

import os
import time
import random
import ctypes
import multiprocessing
from multiprocessing import Pool

def compare_and_swap(sub_array):
    """对子数组进行比较和交换"""
    n = len(sub_array)
    swapped = False
    for i in range(0, n - 1, 2):
        if sub_array[i] > sub_array[i + 1]:
            sub_array[i], sub_array[i + 1] = sub_array[i + 1], sub_array[i]
            swapped = True
    return swapped, sub_array

def parallel_odd_even_sort(arr, num_processes):
    """并行奇偶排序"""
    n = len(arr)
    arr1=arr[:]
    sorted = False

    # 创建进程池，整个排序过程复用
    with Pool(processes=num_processes) as pool:
        while not sorted:
            sorted = True

            # 奇数阶段：从索引 1 开始，确保第一个块长度为奇数，中间块为偶数
            base_chunk_size = (n - 1) // (num_processes*2)
            odd_chunks = []
            start = 1
            for i in range(num_processes):
                end = start + (base_chunk_size)*2
                # 最后一个块可以稍微多一点
                if i == num_processes - 1:
                    end = n if end < n else end
                odd_chunks.append(arr1[start:end])
                start = end

            # 对奇数阶段的分块进行并行处理
            results = pool.map(compare_and_swap, odd_chunks)
            swap_occurred, odd_chunks = zip(*results)
            if any(swap_occurred):
                sorted = False

            # 合并奇数阶段的排序结果回原数组
            arr1[1:n] = [item for chunk in odd_chunks for item in chunk]
            # print(odd_chunks)
            # print(arr1)

            # 偶数阶段：从索引 0 开始，确保第一个块和中间块为偶数长度
            base_chunk_size = n // (num_processes*2)
            even_chunks = []
            start = 0
            for i in range(num_processes):
                end = start + base_chunk_size*2
                # 最后一个块可以稍微多一点
                if i == num_processes - 1:
                    end = n if end < n else end
                even_chunks.append(arr1[start:end])
                start = end

            # 对偶数阶段的分块进行并行处理
            results = pool.map(compare_and_swap, even_chunks)
            swap_occurred, even_chunks = zip(*results)
            if any(swap_occurred):
                sorted = False

            # 合并偶数阶段的排序结果回原数组
            arr1[0:n] = [item for chunk in even_chunks for item in chunk]
            # print("even")
            # print(even_chunks)
            # print(arr1)

    return arr1


def process_all_groups_parallel(data_dir, n_processes):
    group_times = []
    group_cumulative_times = []
    total_cumulative_time = 0

    for group_index in range(10):  # G0 to G9
        print(f"Processing Group G{group_index}")
        group_dir = os.path.join(data_dir, f'G{group_index}')
        group_time = 0

        for array_index in range(8):  # A0 to A7
            print(f"Processing Array A{array_index}")
            array_filename = os.path.join(group_dir, f'A{array_index}.npy')
            Ai = np.load(array_filename)
            Ai_list = Ai.tolist()

            # Record the time before and after sorting
            start_time = time.time()

            sorted_Ai = parallel_odd_even_sort(Ai_list, n_processes)

            end_time = time.time()

            # Calculate time taken to sort this array
            elapsed_time = end_time - start_time
            group_time += elapsed_time

        group_times.append(group_time)
        total_cumulative_time += group_time
        group_cumulative_times.append(total_cumulative_time)

    return group_times, group_cumulative_times

if __name__ == "__main__":
    # Define relative path to the data directory
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.join(current_dir, '..', '..', 'data')  # Path to the 'data' directory

    # Define number of processes to test
    process_counts = [1, 2, 4, 8]  # Adjust based on your CPU cores

    # Store results in a dictionary
    results = {}

    for n_processes in process_counts:
        print(f"\nRunning with {n_processes} processes:")
        group_times, group_cumulative_times = process_all_groups_parallel(data_dir, n_processes)
        results[n_processes] = {'group_times': group_times, 'cumulative': group_cumulative_times}

    # Print the results in the required format
    print("Odd-Even Transposition Sort - C42: Processing time of all groups under multiprocessing implementation")
    header = f"{' ':<10}" + "".join([f"{'Measured MP Time':<68}", f"{'Measured Cumulative MP Time':<68}"])
    subheader = f"{'GrpIndex':<10}" + "".join([f"{p:<17}" for p in process_counts] * 2)
    print(header)
    print(subheader)

    for i in range(10):
        row = f"{i:<10}"
        for p in process_counts:
            row += f"{results[p]['group_times'][i]:<17.12f}"
        for p in process_counts:
            row += f"{results[p]['cumulative'][i]:<17.12f}"
        print(row)
