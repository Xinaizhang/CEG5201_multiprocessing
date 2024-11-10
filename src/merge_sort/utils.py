"""
File: utils.py
Create Date: 2024-10-23
Description:
    - Contains utility functions for merge sort implementation.
"""
from multiprocessing import Pool

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

# Merge sort implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

# Parallel merge sort implementation
def parallel_merge_sort_1(data, pool):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left, right = data[:mid], data[mid:]

    left_sorted, right_sorted = pool.map(merge_sort, [left, right])

    return merge(left_sorted, right_sorted)
