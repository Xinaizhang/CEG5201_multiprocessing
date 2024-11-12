import multiprocessing
import random
import time
import os
from multiprocessing import Pool

def odd_even_sort(arr):
    """
    This function implements the sequential odd-even sorting algorithm. It sorts the array by looping and alternating between the "odd phase" and the "even phase".
    In the "odd phase", it starts at index 1, compares adjacent pairs of elements every two elements, and makes necessary swaps; in the "even phase", it starts at index 0, and compares and swaps in the same way.
    If no swaps occur in a complete odd-even phase traversal, the array is sorted and the loop terminates.
    """
    n = len(arr)
    sorted = False
    while not sorted:
        sorted = True
        
        # Odd phase: start at index 1, compare every two adjacent elements
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False

        # Even phase: start at index 0, compare every two adjacent elements
        for i in range(0, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False
    return arr

def compare_and_swap(sub_array):
    """
    This function is used to compare and exchange adjacent elements in a subarray. It traverses the even index positions of the subarray (starting from index 0, every two positions).
    If the current element is greater than the next element, the positions of the two elements are exchanged and the "whether to exchange" flag is set to True.
    The function returns the subarray and the "whether to exchange" flag to facilitate subsequent judgment of whether to continue sorting.
    """
    n = len(sub_array)
    swapped = False
    for i in range(0, n - 1, 2):
        if sub_array[i] > sub_array[i + 1]:
            sub_array[i], sub_array[i + 1] = sub_array[i + 1], sub_array[i]
            swapped = True
    return swapped, sub_array

def parallel_odd_even_sort(arr, num_processes):
    """
    This function implements a parallel odd-even sorting algorithm, using Python's multiprocessing module to distribute tasks among multiple processes.
    In the odd and even phases, the array is divided into num_processes sub-arrays, and the compare_and_swap function is executed through the process pool to parallelize the comparison and swap operations.
    After each swap, all sub-arrays are merged back into the main array, and whether a swap operation occurs is detected to decide whether to continue sorting.
    The odd and even phases are executed alternately until the sorting is completed.
    """
    n = len(arr)
    arr1=arr[:]
    sorted = False

    with Pool(processes=num_processes) as pool:
        while not sorted:
            sorted = True

            # Odd phase: create sub-arrays for the odd phase
            base_chunk_size = (n - 1) // (num_processes*2)
            odd_chunks = []
            start = 1
            for i in range(num_processes):
                end = start + (base_chunk_size)*2
                if i == num_processes - 1:
                    end = n if end < n else end
                odd_chunks.append(arr1[start:end])
                start = end

            # Process each sub-array in parallel using the process pool
            results = pool.map(compare_and_swap, odd_chunks)
            swap_occurred, odd_chunks = zip(*results)
            if any(swap_occurred):
                sorted = False

            # Merge sorted sub-arrays back into the main array
            arr1[1:n] = [item for chunk in odd_chunks for item in chunk]
            # print(odd_chunks)
            # print(arr1)

            # Even phase: create sub-arrays for the even phase
            base_chunk_size = n // (num_processes*2)
            even_chunks = []
            start = 0
            for i in range(num_processes):
                end = start + base_chunk_size*2
                if i == num_processes - 1:
                    end = n if end < n else end
                even_chunks.append(arr1[start:end])
                start = end

            # Process each sub-array in parallel using the process pool
            results = pool.map(compare_and_swap, even_chunks)
            swap_occurred, even_chunks = zip(*results)
            if any(swap_occurred):
                sorted = False

            # Merge sorted sub-arrays back into the main array
            arr1[0:n] = [item for chunk in even_chunks for item in chunk]
            # print(even_chunks)
            # print(arr1)

    return arr1