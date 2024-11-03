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
    
    # Split the array into halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    # Merge the sorted halves
    return merge(left_half, right_half)

# Parallel merge sort implementation
def parallel_merge_sort(data, pool):
    # 当数据量较小时，直接返回排序后的结果
    if len(data) <= 1:
        return data

    # 递归划分数据集
    mid = len(data) // 2
    left, right = data[:mid], data[mid:]

    # 使用 pool 并行处理左右两半
    left_sorted, right_sorted = pool.map(merge_sort, [left, right])

    # 合并排序后的子数组
    return merge(left_sorted, right_sorted)