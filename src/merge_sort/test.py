import multiprocessing
import random
import time
import os

# 定义合并函数
def merge(left, right):
    sorted_list = []
    i = j = 0

    # 合并两个已排序的子数组
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # 将剩余的元素加入到结果列表中
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

# 改为非递归的并行 merge sort
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

# 单线程的 merge sort，用于 pool 中调用
def merge_sort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)


# 测试并行化的 merge sort 并测量时间
def test_merge_sort_with_processes(data, num_processes):
    start_time = time.time()

    with multiprocessing.Pool(processes=num_processes) as pool:
        sorted_data = parallel_merge_sort(data, pool)

    end_time = time.time()
    print(f"Processes: {num_processes}, Time taken: {end_time - start_time:.4f} seconds")
    return sorted_data

# 主程序
if __name__ == "__main__":
    # 获取逻辑核心数（包括超线程）
    logical_cores = os.cpu_count()
    print(f"Logical cores (including hyper-threading): {logical_cores}")

    # 获取物理核心数（不包括超线程）
    physical_cores = multiprocessing.cpu_count()
    print(f"Physical cores: {physical_cores}")
    
    # 生成随机数向量
    data = [random.randint(1, 1000) for _ in range(1000000)]

    # 测试不同进程数
    for processes in [1, 2, 4, 8]:
        print(f"\nRunning with {processes} processes:")
        sorted_data = test_merge_sort_with_processes(data, processes)
