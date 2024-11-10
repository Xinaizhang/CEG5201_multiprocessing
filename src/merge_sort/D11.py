# D11.py

import pandas as pd
import os
import matplotlib.pyplot as plt

# Define paths to the CSV files
current_dir = os.path.dirname(__file__)
data_dir = os.path.join(current_dir, 'data')
b11_file = os.path.join(data_dir, 'B11_G0_processing_times.csv')
c11_file = os.path.join(data_dir, 'C11_G0_parallel_processing_times.csv')

# Load CSV data
b11_data = pd.read_csv(b11_file)
c11_data = pd.read_csv(c11_file)

# Print column names to debug the error
print("Columns in C11 data:", c11_data.columns)

# Define process counts to analyze, excluding process=1
process_counts = [2, 4, 8]

# Calculate individual array speed-ups and cumulative speed-ups
array_speedup_results = {count: [] for count in process_counts}  # Individual array speed-ups
cumulative_speedup_results = {count: [] for count in process_counts}  # Cumulative speed-ups

# Calculate speed-up for each array and each process count
for count in process_counts:
    cumulative_b11_time = 0
    cumulative_c11_time = 0
    for i in range(8):  # Assuming arrays A0 to A7
        # Individual speed-up
        sequential_time = b11_data['Measured Sequential Time'].iloc[i]
        # Adjust column name based on actual data
        parallel_time = c11_data[f'Time_{count}P'].iloc[i]
        speedup = sequential_time / parallel_time
        array_speedup_results[count].append(speedup)
        
        # Cumulative speed-up
        cumulative_b11_time += sequential_time
        cumulative_c11_time += parallel_time
        cumulative_speedup = cumulative_b11_time / cumulative_c11_time
        cumulative_speedup_results[count].append(cumulative_speedup)

# Plot Measured Speed-Up for Each Array (process counts 2, 4, 8)
plt.figure(figsize=(10, 6))
for count in process_counts:
    plt.plot(range(8), array_speedup_results[count], marker='o', label=f'Processor={count} Measured Speed Up')
plt.xlabel('Array')
plt.ylabel('Measured Speed Up')
plt.title('Measured Speed Up With Different Processor Numbers')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the first plot
measured_speedup_plot_file = os.path.join(data_dir, 'D11_measured_speedup_plot.png')
plt.savefig(measured_speedup_plot_file)
print(f"Measured Speed-Up plot saved to {measured_speedup_plot_file}")

# Plot Cumulative Speed-Up for Each Array (process counts 2, 4, 8)
plt.figure(figsize=(10, 6))
for count in process_counts:
    plt.plot(range(8), cumulative_speedup_results[count], marker='o', label=f'Processor={count} Cumulative Speed Up')
plt.xlabel('Array')
plt.ylabel('Cumulative Speed Up')
plt.title('Cumulative Speed Up With Different Processor Numbers')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the second plot
cumulative_speedup_plot_file = os.path.join(data_dir, 'D11_cumulative_speedup_plot.png')
plt.savefig(cumulative_speedup_plot_file)
print(f"Cumulative Speed-Up plot saved to {cumulative_speedup_plot_file}")

# Save speed-up results to CSV
speedup_output_file = os.path.join(data_dir, 'D11_G0_speedup.csv')

# Create DataFrame for array and cumulative speed-ups
array_speedup_df = pd.DataFrame(array_speedup_results, index=[f'Array A{i}' for i in range(8)])
cumulative_speedup_df = pd.DataFrame(cumulative_speedup_results, index=[f'Array A{i}' for i in range(8)])

# Concatenate and save
speedup_df = pd.concat([array_speedup_df.add_prefix('Measured Speed Up '), cumulative_speedup_df.add_prefix('Cumulative Speed Up ')], axis=1)
speedup_df.to_csv(speedup_output_file)
print(f"Speed-up results saved to {speedup_output_file}")
