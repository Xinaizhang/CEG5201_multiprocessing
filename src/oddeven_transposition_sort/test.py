import multiprocessing
import random
import time
import os
from multiprocessing import Pool, Array
import ctypes

def odd_even_sort(arr):
    n = len(arr)
    sorted = False
    while not sorted:
        sorted = True
        
        # 奇数阶段
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False

        # 偶数阶段
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False
    return arr



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










# 主程序
if __name__ == "__main__":
    # 获取逻辑核心数（包括超线程）
    logical_cores = os.cpu_count()
    print(f"Logical cores (including hyper-threading): {logical_cores}")

    # 获取物理核心数（不包括超线程）
    physical_cores = multiprocessing.cpu_count()
    print(f"Physical cores: {physical_cores}")
    
    # 生成随机数向量
    data = [random.randint(1, 255) for _ in range(8000)]
    
    # 测试不同进程数
    for processes in [1, 2, 4, 8]:
        print(f"\nRunning with {processes} processes:")
        # print(data)
        start_time = time.time()
        sorted_data = parallel_odd_even_sort(data, processes)
        end_time = time.time()
        # print(sorted_data)
        print("Execution time:", end_time - start_time)
