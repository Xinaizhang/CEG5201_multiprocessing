"""
File: utilsv2.py
Create Date: 2024-10-30
Description:
    - Contains utility functions for merge sort implementation.
"""
from multiprocessing import Pool, current_process
import os

pool = None

def init_pool(p):
    global pool
    pool = p

def merge(left, right):
    result = []
    i = j = 0

    # Merge two sorted arrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def parallel_merge_sort(arr, depth=0, max_depth=3):
    if len(arr) <= 1:
        return arr

    if depth >= max_depth:
        return merge_sort(arr)

    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]

    if pool is not None and current_process().name == 'MainProcess':
        left_result = pool.apply_async(parallel_merge_sort, args=(left, depth+1, max_depth))
        right_result = pool.apply_async(parallel_merge_sort, args=(right, depth+1, max_depth))

        left_sorted = left_result.get()
        right_sorted = right_result.get()
    else:
        left_sorted = parallel_merge_sort(left, depth+1, max_depth)
        right_sorted = parallel_merge_sort(right, depth+1, max_depth)

    return merge(left_sorted, right_sorted)
