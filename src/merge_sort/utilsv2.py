from multiprocessing import Pool, current_process
import os

# Global variable to hold the pool
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

# Sequential merge sort implementation
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
        # Exceeded max depth, use sequential merge_sort
        return merge_sort(arr)

    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]

    if pool is not None and current_process().name == 'MainProcess':
        # Use apply_async in the main process
        left_result = pool.apply_async(parallel_merge_sort, args=(left, depth+1, max_depth))
        right_result = pool.apply_async(parallel_merge_sort, args=(right, depth+1, max_depth))

        # Get results
        left_sorted = left_result.get()
        right_sorted = right_result.get()
    else:
        # Sequential recursion in child processes
        left_sorted = parallel_merge_sort(left, depth+1, max_depth)
        right_sorted = parallel_merge_sort(right, depth+1, max_depth)

    # Merge results
    return merge(left_sorted, right_sorted)
