# D12.py

import pandas as pd
import os
import matplotlib.pyplot as plt

# Define paths to the CSV files
current_dir = os.path.dirname(__file__)
data_dir = os.path.join(current_dir, 'data')
b12_file = os.path.join(data_dir, 'B12_all_groups_processing_times.csv')
c12_file = os.path.join(data_dir, 'C12_all_groups_parallel_processing_times.csv')

# Load CSV data
b12_data = pd.read_csv(b12_file)
c12_data = pd.read_csv(c12_file)

# Define process counts to analyze, excluding process=1
process_counts = [2, 4, 8]

# Calculate individual group speed-ups and cumulative speed-ups
group_speedup_results = {count: [] for count in process_counts}  # Individual group speed-ups
cumulative_speedup_results = {count: [] for count in process_counts}  # Cumulative speed-ups

# Calculate speed-up for each group and each process count
for count in process_counts:
    cumulative_b12_time = 0
    cumulative_c12_time = 0
    for i in range(10):  # Assuming groups G0 to G9
        # Individual speed-up
        sequential_time = b12_data['Sequential Time (Group)'].iloc[i]
        parallel_time = c12_data[f'Time_{count}P'].iloc[i]
        speedup = sequential_time / parallel_time
        group_speedup_results[count].append(speedup)
        
        # Cumulative speed-up
        cumulative_b12_time += sequential_time
        cumulative_c12_time += parallel_time
        cumulative_speedup = cumulative_b12_time / cumulative_c12_time
        cumulative_speedup_results[count].append(cumulative_speedup)

# Plot Measured Speed-Up for Each Group (process counts 2, 4, 8)
plt.figure(figsize=(10, 6))
for count in process_counts:
    plt.plot(range(10), group_speedup_results[count], marker='o', label=f'Processor={count} Measured Speed Up')
plt.xlabel('Group')
plt.ylabel('Measured Speed Up')
plt.title('Measured Speed Up With Different Processor Numbers')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the first plot
measured_speedup_plot_file = os.path.join(data_dir, 'D12_measured_speedup_plot.png')
plt.savefig(measured_speedup_plot_file)
print(f"Measured Speed-Up plot saved to {measured_speedup_plot_file}")

# Plot Cumulative Speed-Up for Each Group (process counts 2, 4, 8)
plt.figure(figsize=(10, 6))
for count in process_counts:
    plt.plot(range(10), cumulative_speedup_results[count], marker='o', label=f'Processor={count} Cumulative Speed Up')
plt.xlabel('Group')
plt.ylabel('Cumulative Speed Up')
plt.title('Cumulative Speed Up With Different Processor Numbers')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the second plot
cumulative_speedup_plot_file = os.path.join(data_dir, 'D12_cumulative_speedup_plot.png')
plt.savefig(cumulative_speedup_plot_file)
print(f"Cumulative Speed-Up plot saved to {cumulative_speedup_plot_file}")

# Save speed-up results to CSV
speedup_output_file = os.path.join(data_dir, 'D12_all_groups_speedup.csv')

# Create DataFrame for group and cumulative speed-ups
group_speedup_df = pd.DataFrame(group_speedup_results, index=[f'Group {i}' for i in range(10)])
cumulative_speedup_df = pd.DataFrame(cumulative_speedup_results, index=[f'Group {i}' for i in range(10)])

# Concatenate and save
speedup_df = pd.concat([group_speedup_df.add_prefix('Measured Speed Up '), cumulative_speedup_df.add_prefix('Cumulative Speed Up ')], axis=1)
speedup_df.to_csv(speedup_output_file)
print(f"Speed-up results saved to {speedup_output_file}")
