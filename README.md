# NUS CEG5201 CA2 - Group6

## 1. Merge sort -> ZXA
## 2. Bucket sort -> YY
## 3. Quicksort -> HRQ
### 1. Sequential Sorting Array in Group 0 (`b31.py`)

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


### 2. Sequential Sorting All Groups (b32.py)
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


### 3. Parallel Sorting All Groups (c31_c32.py)

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



## 4. Odd-even transposition sort -> YJH

- Hardware platform: CPU