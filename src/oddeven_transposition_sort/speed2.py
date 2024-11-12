import numpy as np
import matplotlib.pyplot as plt

# 生成示例耗时数据（单位：秒），表示顺序算法和不同进程数的并行算法在不同数组大小下的耗时
array_indices = np.arange(10)
sequential_time = np.array([
    2.990797, 2.985932, 3.023166, 3.042537, 2.982574,3.011486, 2.997341, 2.974803, 3.040280, 3.078148
])
parallel_times = {
    1: np.array([12.413133, 12.749444, 13.133534, 12.450486, 12.056199, 12.068931, 12.361463, 12.300378, 12.296615, 12.387727]),
    2: np.array([8.387355, 8.346916, 8.379151, 8.361048, 8.301793, 8.354912, 8.341847, 8.361098, 8.300156, 8.416029]),
    4: np.array([8.939562, 8.933834, 8.934188, 9.077512, 8.909577, 8.936216, 8.902194, 8.914448, 8.837643, 8.960037]),
    8: np.array([11.931434, 11.877280, 11.970814, 12.005474, 11.797779, 11.850287, 11.813502, 11.725693, 11.641039, 11.669459])
}


# 计算加速比
speed_ups = {p: sequential_time / parallel_times[p] for p in parallel_times}

# 创建图像和子图
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 绘制加速比图（左图）
for process_count in parallel_times.keys():
    axes[0].plot(array_indices, speed_ups[process_count], marker='o', label=f'Processes={process_count}')

axes[0].set_title("Measured Speed-Up with Different Processor Numbers (D42)")
axes[0].set_xlabel("Group Index")
axes[0].set_ylabel("Measured Speed-Up")
axes[0].legend()
axes[0].grid(True)

# 计算新的累计加速比并绘制图（右图）
for process_count in parallel_times.keys():
    cumulative_speed_up = [
        np.sum(sequential_time[:i+1]) / np.sum(parallel_times[process_count][:i+1])
        for i in range(len(array_indices))
    ]
    axes[1].plot(array_indices, cumulative_speed_up, marker='o', label=f'Processes={process_count}')

axes[1].set_title("Cumulative Speed-Up with Different Processor Numbers (D42)")
axes[1].set_xlabel("Group Index")
axes[1].set_ylabel("Cumulative Speed-Up")
axes[1].legend()
axes[1].grid(True)

# 显示图像
plt.tight_layout()
plt.show()
