from multiprocessing import Pool

# Prepare buckets
def prepare_buckets(arr, N=10):
    # Create N empty buckets
    buckets = [[] for _ in range(N)]
    max_value, min_value = max(arr), min(arr)
    bucket_range = (max_value - min_value) / N
    # Distribute elements into buckets
    for num in arr:
        idx = int((num - min_value) / bucket_range)
        if idx == N:
            idx -= 1
        buckets[idx].append(num)
    return buckets

# Sort a single bucket
def sort_bucket(bucket):
    return sorted(bucket)

# Sequential processing
def sequential_bucket_sort(arr):
    buckets = prepare_buckets(arr)
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))
    return sorted_array

# Parallel processing
def parallel_bucket_sort(arr, num_processes):
    buckets = prepare_buckets(arr)
    with Pool(processes=num_processes) as pool:
        sorted_buckets = pool.map(sort_bucket, buckets)
    sorted_array = []
    for bucket in sorted_buckets:
        sorted_array.extend(bucket)
    return sorted_array