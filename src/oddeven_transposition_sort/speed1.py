

import numpy as np
import matplotlib.pyplot as plt

# 生成示例耗时数据（单位：秒），表示顺序算法和不同进程数的并行算法在不同数组大小下的耗时
array_indices = np.arange(8)
sequential_time = np.array([0.000000, 0.000000, 0.000000, 0.000000, 0.047487, 0.125617, 0.556648, 2.274926])
parallel_times = {
    1: np.array([0.152203, 0.140576, 0.152229, 0.197839, 0.303556, 0.749022, 2.159327, 7.705301]),
    2: np.array([0.150111, 0.145596, 0.169321, 0.222673, 0.333342, 0.674181, 1.741379, 5.540672]),
    4: np.array([0.206013, 0.162043, 0.210272, 0.275901, 0.444220, 0.821987, 1.875224, 5.102461]),
    8: np.array([0.191268, 0.223526, 0.252437, 0.425178, 0.658303, 1.269335, 2.535793, 6.695473])
}

# 计算加速比
speed_ups = {p: sequential_time / parallel_times[p] for p in parallel_times}

# 创建图像和子图
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 绘制加速比图（左图）
for process_count in parallel_times.keys():
    axes[0].plot(array_indices, speed_ups[process_count], marker='o', label=f'Processes={process_count}')

axes[0].set_title("Measured Speed-Up with Different Processor Numbers (D41)")
axes[0].set_xlabel("Array Index in G0")
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

axes[1].set_title("Cumulative Speed-Up with Different Processor Numbers (D41)")
axes[1].set_xlabel("Array Index in G0")
axes[1].set_ylabel("Cumulative Speed-Up")
axes[1].legend()
axes[1].grid(True)

# 显示图像
plt.tight_layout()
plt.show()

