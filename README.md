# NUS CEG5201 CA2 - Group6

## 1. Merge sort (A0296854J_ZhangXinai)

**Setup**: 
Navigate to the Merge Sort directory before executing the scripts:
```bash
cd src/merge_sort
```

### 1.1 `utils.py` and `utilsv2.py`

These files provide core utilities for implementing Merge Sort, including both sequential and parallel sorting functions. `utils.py` includes a basic Merge Sort, while `utilsv2.py` provides an optimized parallel Merge Sort with adjustable depth control.

#### Key Functions
1. **`merge(left, right)`**:
   - Merges two sorted subarrays into one sorted array, used in both sequential and parallel sorts.

2. **`merge_sort(arr)`**:
   - Implements a recursive, sequential Merge Sort, dividing the array into halves and recursively sorting and merging.

3. **`parallel_merge_sort(arr, depth=0, max_depth=3)`** (`utilsv2.py`):
   - Recursive parallel Merge Sort with controlled depth to optimize performance. The `max_depth` parameter limits recursion depth to manage parallelism effectively and prevent resource overuse.

#### Usage
- **Importing**:
  - Sequential and parallel sorting functions can be imported as needed:
    ```python
    from utils import merge_sort  # Sequential sorting
    from utilsv2 import parallel_merge_sort  # Parallel sorting
    ```

- **Dependencies**:
  - `multiprocessing` (standard Python library) for parallel processing.


### 1.2 Sequential Sorting (`B11.py` and `B12.py`)

Scripts `B11.py` and `B12.py` use sequential Merge Sort to process datasets of arrays, measuring execution time for each array and providing cumulative timing information. Each script processes `.npy` files within specified directories, tracking both individual and cumulative sorting times.

#### `B11.py`: Processing Group `G0`
- **Functionality**:
  - Processes a single group (`G0`), containing arrays `A0` to `A7`, using sequential Merge Sort.
  - For each array, it records sorting time and cumulative time, outputting results to both console and a CSV file.

- **Usage**:
```bash
python B11.py
```
- **Input Requirements**:
  - Arrays must be located in the `data/G0` directory.
- **Output**:
  - Results saved in `B11_G0_processing_times.csv`, showing individual and cumulative sorting times for each array.
- **Dependencies**:
  - `numpy` (for loading `.npy` files): install via `pip install numpy`
  - `os`, `time`, `csv` (standard Python libraries)

#### `B12.py`: Processing Groups `G0` to `G9`
- **Functionality**:
  - Processes groups `G0` to `G9`, sequentially sorting each array within each group.
  - Records total sorting time per group and cumulative time across all groups.
- **Usage**:
```bash
python B12.py
```
- **Input Requirements**:
  - Groups `G0` to `G9` should be organized within the data directory, each containing arrays `A0` to `A7`.
- **Output**:
  - Results saved in `B12_all_groups_processing_times.csv`, detailing individual group processing times and cumulative times across groups.

### 1.3 Parallel Sorting All Groups
#### **Version 1**: Chunk-Based Parallel Merge Sort (`C11_v1.py` & `C12_v1.py`)

This version of the parallel Merge Sort uses chunk-based parallel processing to divide and sort parts of each array or group. Arrays are split into chunks processed in parallel by a specified number of processes, improving efficiency by distributing work across multiple cores.

- **`C11_v1.py`**: Processes group `G0` using chunk-based parallel Merge Sort.
  - Arrays (`A0` to `A7`) are divided into chunks, sorted independently in parallel, and merged iteratively.
  - **Input**: Expects `.npy` array files in `data/G0`.
  - **Parameters**: The number of processes to test is set as `[1, 2, 4, 8]`.
  - **Output**: Prints individual and cumulative processing times for each array and saves results to a CSV file (`C11_G0_parallel_processing_times.csv`).

- **`C12_v1.py`**: Extends the chunk-based parallel approach to all groups (`G0` to `G9`).
  - Sequentially processes each group using the chunk-based parallel Merge Sort, printing and saving cumulative processing times for each group.
  - **Input**: Expects `G0` to `G9` directories in `data`.
  - **Output**: Prints results and saves cumulative times for each group to a CSV file (`C12_all_groups_parallel_processing_times.csv`).

**Usage**:
```bash
python C11_v1.py
python C12_v1.py
```
#### **Version 2**: Recursive Parallel Merge Sort with Controlled Depth (`C11_v2.py` & `C12_v2.py`)
This version uses a recursive parallel Merge Sort with controlled depth to manage resource allocation. By limiting recursion depth, this method reduces overhead and balances efficiency across multiple processes.
- `C11_v2.py`: Processes group `G0` using recursive parallel Merge Sort.
  - Uses a `max_depth` parameter (based on the number of processes) to control parallel recursion.
  - Input: Expects `.npy` files for arrays `A0` to `A7` in `data/G0`.
  - Parameters: The number of processes is set as `[1, 2, 4, 8]`.
  - Output: Prints and saves processing times for each array in `C11_G0_parallel_processing_times.csv`.
- `C12_v2.py`: Extends the recursive approach to all groups (`G0` to `G9`).
  - Recursively processes each array in all groups, with max_depth adjusted by the number of processes.
  - Input: Expects directories for each group (`G0` to `G9`) in data.
  - Output: Prints and saves cumulative processing times for each group in `C12_all_groups_parallel_processing_times.csv`.
**Usage**:
```bash
python C11_v2.py
python C12_v2.py
```

### 1.4 Draw the Speed-Up Figure (`D11.py` & `D12.py`)
The scripts `D11.py` and `D12.py` visualize the performance of parallel processing by plotting speed-up graphs for different process counts.

- `D11.py`: Generates speed-up plots for individual arrays and cumulative speed-ups for group G0.
  - **Input**: Requires timing data from B11_G0_processing_times.csv (sequential) and C11_G0_parallel_processing_times.csv (parallel).
  - **Output**: Creates two plots (measured and cumulative speed-ups) saved as D11_measured_speedup_plot.png and D11_cumulative_speedup_plot.png.
  - **Additional Output**: Saves detailed speed-up results for each process count in D11_G0_speedup.csv.
- `D12.py`: Extends the speed-up analysis to all groups (G0 to G9).
  - **Input**: Requires timing data from B12_all_groups_processing_times.csv and C12_all_groups_parallel_processing_times.csv.
  - **Output**: Creates speed-up plots for each group and cumulative speed-ups across all groups, saved as D12_measured_speedup_plot.png and D12_cumulative_speedup_plot.png.
  - **Additional Output**: Saves detailed speed-up results for each process count in D12_all_groups_speedup.csv.
**Usage**:
```bash
python D11.py
python D12.py
```


## 2. Bucket sort -> YY



## 3. Quicksort -> (A0296346R_Hou Runqi)
### 3.1 Sequential Sorting Array in Group 0 (`b31.py`)

This file sequential sort array from group 0 using a sequental quicksort algorithm and logs the sorting times.

#### Functions
- **`load_arrays(group_dir)`**: 
  - Loads the `.npy` files from the specified group directory.
  - **Parameters**: `group_dir` (str) - The directory path containing the `.npy` files.
  - **Returns**: A list of loaded arrays.

- **`quicksort(arr)`**: 
  - A recursive implementation of quicksort.
  - **Parameters**: `arr` (list) - The list of numbers to sort.
  - **Returns**: A sorted list.

- **`log_time(log_file, message)`**: 
  - Appends a message to the specified log file.
  - **Parameters**:
    - `log_file` (str) - Path to the log file.
    - `message` (str) - The message to log.

#### Usage
- Configure the `num_groups` and `num_arrays` variables to specify the number of groups and arrays.
- Run the script:
  ```bash
  python b31.py
- Check the log file (sorting_times_b31.log).
    ```sql
    Processing group 0:
    Array A0 sorted in 0.00007380000000001274 seconds. Cumulative Sequential time in 0.00007380000000001274 seconds.
    Array A1 sorted in 0.00013070000000001136 seconds. Cumulative Sequential time in 0.00020450000000002411 seconds.
    ...
    Array A7 sorted in 0.00637599999999999278 seconds. Cumulative Sequential time in 0.01411510000000004705 seconds.
    
    Overall sequential sorting time for all groups: 0.01411510000000004705 seconds.


### 3.2 Sequential Sorting All Groups (b32.py)
This file sequential sort all groups using a sequential quicksort algorithm and logs the sorting times.
#### Functions
- **`load_arrays(group_dir)`**: 
  - Loads the `.npy` files from the specified group directory.
  - **Parameters**: `group_dir` (str) - The directory path containing the `.npy` files.
  - **Returns**: A list of loaded arrays.

- **`quicksort(arr)`**: 
  - A recursive implementation of quicksort.
  - **Parameters**: `arr` (list) - The list of numbers to sort.
  - **Returns**: A sorted list.

- **`log_time(log_file, message)`**: 
  - Appends a message to the specified log file.
  - **Parameters**:
    - `log_file` (str) - Path to the log file.
    - `message` (str) - The message to log.

#### Usage
- Run the script:
  ```bash
  python b32.py
- Check the log file (sorting_times_b31.log).
    ```sql
    Processing group 0 from ../../data/G0:
    Array 1 sorted in 0.00014719999999998623 seconds. Cumulative Sequential time in 0.00014719999999998623 seconds.
    ...
    Array 8 sorted in 0.00893369999999998887 seconds. Cumulative Sequential time in 0.02376779999999995008 seconds.
    Total sequential sorting time for group 0: 0.02376779999999995008 seconds.
    Processing group 1 from ../../data/G1:
    Array 1 sorted in 0.00012909999999999311 seconds. Cumulative Sequential time in 0.00012909999999999311 seconds.
    ...
    Array 8 sorted in 0.00683100000000000374 seconds. Cumulative Sequential time in 0.01473139999999997785 seconds.


### 3.3 Parallel Sorting All Groups (c31_c32.py)

### Functions
- **`load_arrays(group_dir)`**: 
  - Loads the `.npy` files from the specified group directory.
  - **Parameters**: `group_dir` (str) - The directory path containing the `.npy` files.
  - **Returns**: A list of loaded arrays.

- **`quicksort(arr)`**: 
  - A recursive implementation of quicksort.
  - **Parameters**: `arr` (list) - The list of numbers to sort.
  - **Returns**: A sorted list.

- **`partition_data(arr, pivot)`**:
  - Splits an array into two lists based on a pivot value.
  - **Parameters**:
    - `arr` (list) - The list of numbers to partition.
    - `pivot` (int) - The pivot value.
  - **Returns**: Two lists, `low` and `high`, containing elements less than or equal to, and greater than the pivot, respectively.

- **`parallel_quicksort(arr, n_processes)`**:
  - A parallel quicksort function that utilizes multiple processes to sort the array.
  - **Parameters**:
    - `arr` (list) - The list of numbers to sort.
    - `n_processes` (int) - The number of processes to use for parallel sorting.
  - **Returns**: A sorted list.

- **`log_time(log_file, message)`**: 
  - Appends a message to the specified log file.
  - **Parameters**:
    - `log_file` (str) - Path to the log file.
    - `message` (str) - The message to log.

#### Usage
- Run the script:
  ```bash
  python c31_c32.py
- Check the log file (sorting_times_c32.log).
    ```sql
    Processing group 0 with processor 1:
    0.44518140000000006040
    ...
    0.47240159999999997709
    Processing group 0 with processor 1:
    0.44518140000000006040
    ...
    3.47493209999999974613
    group0 done takes 3.47493209999999974613
- The first block of time is the array time and second block of time is the cumulative time sorting each array. It shows the group information and processor information.

### 3.4 Draw the Speed Up Figure (D1.py D2.py)
#### Usage
- Run the script:
  ```bash
  python D1.py
  python D2.py
- Load and preprocess data from d1.xlsx.
- Plot two graphs:
  - Measured Speed-Up with different processor numbers.
  - Cumulative Speed-Up with different processor numbers.

## 4. Odd-even transposition sort -> (A0298720W_YangJunheng)

### 4.0 Preparation

#### Install Dependencies
The python packages you need to use are: multiprocessing, numpy, os, time, csv, matplotlib, you can install them directly using "pip install".

**Setup**: 
Navigate to the Merge Sort directory before executing the scripts:
```bash
cd src/oddeven_transposition_sort
```

### 4.1 `utils.py`

These files provide core utilities for implementing Odd-even transposition sort , including both sequential and parallel sorting functions. 

#### Key Functions
1. **`odd_even_sort(arr)`**:
    - Execute the odd-even sorting algorithm sequentially.
    - **Parameters**: `arr` (list) - Original array
    - **Returns**: Sorted array

2. **`parallel_odd_even_sort(arr, num_processes)`**:
    - Execute the odd-even sorting algorithm in parallel.
    - **Parameters**:
      - `arr` (list) - Original array
      - `num_processes` (int) - The number of process.
    - **Returns**: Sorted array

3. **`compare_and_swap(sub_array)`**:
    - Perform a sorted traversal of each subarray in the parallel algorithm (that is, only traverse once, and the returned result is not necessarily an ordered array).
    - **Parameters**: `sub_array` (list) - Original subarray
    - **Returns**: The flag indicating whether data exchange occurs and the sub-array after one traversal.

#### Usage
- **Importing**:
  - Sequential and parallel sorting functions can be imported as needed:
    ```python
    from utils import odd_even_sort  # Sequential sorting
    from utils import parallel_odd_even_sort  # Parallel sorting
    ```


### 4.2 Sequential Sorting (`B41.py` and `B42.py`)

Scripts `B41.py` and `B42.py` use sequential Odd-even transposition sort to process datasets of arrays, measuring execution time for each array and providing cumulative timing information. Each script processes `.npy` files within specified directories, tracking both individual and cumulative sorting times. And store the results in B41.csv and B42.csv in the data folder.

#### `B41.py`: Processing Group `G0`
- **Functionality**:
  - Processes a single group (`G0`), cdontaining arrays `A0` to `A7`, using sequential Odd-even transposition sort. And store the results in B41.csv in the data folder.

- **Usage**:
```bash
python B41.py
```

#### `B42.py`: Processing Groups `G0` to `G9`
- **Functionality**:
  - Processes groups `G0` to `G9`, sequentially sorting each array within each group. And store the results in B42.csv in the data folder.
- **Usage**:
```bash
python B42.py
```

### 4.3 Parallel Sorting(`C41.py` & `C42.py`)

Scripts `C41.py` and `C42.py` use parallel Odd-even transposition sort to process datasets of arrays, measuring execution time for each array and providing cumulative timing information. Each script processes `.npy` files within specified directories, tracking both individual and cumulative sorting times. And store the results in C41.csv and C42.csv in the data folder.

#### `C41.py`: Processing Group `G0`
- **Functionality**:
  - Processes a single group (`G0`), cdontaining arrays `A0` to `A7`, using parallel Odd-even transposition sort. And store the results in C41.csv in the data folder.

- **Usage**:
```bash
python C41.py
```

#### `C42.py`: Processing Groups `G0` to `G9`
- **Functionality**:
  - Processes groups `G0` to `G9`, sorting each array within each group in parallel. And store the results in C42.csv in the data folder.
- **Usage**:
```bash
python C42.py
```


### 4.4 Draw the Speed-Up Figure (`D41.py` & `D42.py`)
The scripts `D41.py` and `D42.py` visualize the performance of parallel processing by plotting speed-up graphs for different process counts.

- `D41.py`: Generates speed-up plots for individual arrays and cumulative speed-ups for group G0.
  - **Input**: Requires B41.csv and C41.csv.
  - **Output**: Creates two plots (measured and cumulative speed-ups).
- `D42.py`: Extends the speed-up analysis to all groups (G0 to G9).
  - **Input**: Requires B42.csv and C42.csv.
  - **Output**: Creates speed-up plots for each group and cumulative speed-ups across all groups.
**Usage**:
```bash
python D41.py
python D42.py
```