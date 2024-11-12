import multiprocessing
import random
import time
import os

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
