import multiprocessing
import random
import time
import os
from multiprocessing import Pool

def odd_even_sort(arr):
    n = len(arr)
    sorted = False
    while not sorted:
        sorted = True

        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False

        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False
    return arr

def compare_and_swap(sub_array):
    n = len(sub_array)
    swapped = False
    for i in range(0, n - 1, 2):
        if sub_array[i] > sub_array[i + 1]:
            sub_array[i], sub_array[i + 1] = sub_array[i + 1], sub_array[i]
            swapped = True
    return swapped, sub_array

def parallel_odd_even_sort(arr, num_processes):
    n = len(arr)
    arr1=arr[:]
    sorted = False

    with Pool(processes=num_processes) as pool:
        while not sorted:
            sorted = True

            base_chunk_size = (n - 1) // (num_processes*2)
            odd_chunks = []
            start = 1
            for i in range(num_processes):
                end = start + (base_chunk_size)*2
                if i == num_processes - 1:
                    end = n if end < n else end
                odd_chunks.append(arr1[start:end])
                start = end

            results = pool.map(compare_and_swap, odd_chunks)
            swap_occurred, odd_chunks = zip(*results)
            if any(swap_occurred):
                sorted = False

            arr1[1:n] = [item for chunk in odd_chunks for item in chunk]
            # print(odd_chunks)
            # print(arr1)

            base_chunk_size = n // (num_processes*2)
            even_chunks = []
            start = 0
            for i in range(num_processes):
                end = start + base_chunk_size*2
                if i == num_processes - 1:
                    end = n if end < n else end
                even_chunks.append(arr1[start:end])
                start = end

            results = pool.map(compare_and_swap, even_chunks)
            swap_occurred, even_chunks = zip(*results)
            if any(swap_occurred):
                sorted = False

            arr1[0:n] = [item for chunk in even_chunks for item in chunk]
            # print(even_chunks)
            # print(arr1)

    return arr1