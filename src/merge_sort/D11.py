import pandas as pd
import os
import matplotlib.pyplot as plt

current_dir = os.path.dirname(__file__)
data_dir = os.path.join(current_dir, 'data')
b11_file = os.path.join(data_dir, 'B11_G0_processing_times.csv')
c11_file = os.path.join(data_dir, 'C11_G0_parallel_processing_times.csv')

b11_data = pd.read_csv(b11_file)
c11_data = pd.read_csv(c11_file)

print("Columns in C11 data:", c11_data.columns)

process_counts = [2, 4, 8]
array_speedup_results = {count: [] for count in process_counts}
cumulative_speedup_results = {count: [] for count in process_counts}

for count in process_counts:
    cumulative_b11_time = 0
    cumulative_c11_time = 0
    for i in range(8):
        sequential_time = b11_data['Measured Sequential Time'].iloc[i]
        parallel_time = c11_data[f'Time_{count}P'].iloc[i]
        speedup = sequential_time / parallel_time
        array_speedup_results[count].append(speedup)
        
        cumulative_b11_time += sequential_time
        cumulative_c11_time += parallel_time
        cumulative_speedup = cumulative_b11_time / cumulative_c11_time
        cumulative_speedup_results[count].append(cumulative_speedup)

plt.figure(figsize=(10, 6))
for count in process_counts:
    plt.plot(range(8), array_speedup_results[count], marker='o', label=f'Processor={count} Measured Speed Up')
plt.xlabel('Array')
plt.ylabel('Measured Speed Up')
plt.title('Measured Speed Up With Different Processor Numbers')
plt.legend()
plt.grid(True)
plt.tight_layout()

measured_speedup_plot_file = os.path.join(data_dir, 'D11_measured_speedup_plot.png')
plt.savefig(measured_speedup_plot_file)
print(f"Measured Speed-Up plot saved to {measured_speedup_plot_file}")

plt.figure(figsize=(10, 6))
for count in process_counts:
    plt.plot(range(8), cumulative_speedup_results[count], marker='o', label=f'Processor={count} Cumulative Speed Up')
plt.xlabel('Array')
plt.ylabel('Cumulative Speed Up')
plt.title('Cumulative Speed Up With Different Processor Numbers')
plt.legend()
plt.grid(True)
plt.tight_layout()

cumulative_speedup_plot_file = os.path.join(data_dir, 'D11_cumulative_speedup_plot.png')
plt.savefig(cumulative_speedup_plot_file)
print(f"Cumulative Speed-Up plot saved to {cumulative_speedup_plot_file}")

speedup_output_file = os.path.join(data_dir, 'D11_G0_speedup.csv')
array_speedup_df = pd.DataFrame(array_speedup_results, index=[f'Array A{i}' for i in range(8)])
cumulative_speedup_df = pd.DataFrame(cumulative_speedup_results, index=[f'Array A{i}' for i in range(8)])

speedup_df = pd.concat([array_speedup_df.add_prefix('Measured Speed Up '), cumulative_speedup_df.add_prefix('Cumulative Speed Up ')], axis=1)
speedup_df.to_csv(speedup_output_file)
print(f"Speed-up results saved to {speedup_output_file}")
