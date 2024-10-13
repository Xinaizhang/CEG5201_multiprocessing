"""
File: data_generation.py
Create Date: 2024-10-13
Description:
    - Generate 8 unsorted array instances, denoted as Ai where i ∈ [0, 1, … 7]. 
    - The length denoted by Ni of each array instance Ai is chosen from the set {64, 128, 256, 512, 1024, 2048, 4096, 8192}. 
    - Note that the value of each element Ai[j], should be between 0 and 255 (random integers only). 
    - Next, generate 10 groups of such list of arrays Gj, j ∈ [0, 1, … 9]. 
    - All the team members need to use the same set of G for their subsequent tasks.
"""
import numpy as np
import os

# Set the random seed for reproducibility so that all team members generate the same data
np.random.seed(0)

# Define the possible lengths Ni for the arrays Ai
lengths = [64, 128, 256, 512, 1024, 2048, 4096, 8192]

# Number of groups Gj to generate
num_groups = 10

# Number of arrays Ai in each group
num_arrays = 8

# Create a directory named 'data' to save the generated arrays
data_dir = 'data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Loop over each group Gj
for group_index in range(num_groups):
    # Create a subdirectory for each group within the 'data' directory
    # The subdirectory is named 'G0', 'G1', ..., 'G9' for groups G0 to G9
    group_dir = os.path.join(data_dir, f'G{group_index}')
    if not os.path.exists(group_dir):
        os.makedirs(group_dir)
    
    print(f'Generating data for group G{group_index}')
    
    # Loop over each array Ai in the group
    for array_index in range(num_arrays):
        # Select the length Ni for this array from the predefined lengths list
        # The lengths are assigned in order, so Ai has length lengths[i]
        Ni = lengths[array_index]
        
        # Generate an unsorted array Ai of length Ni with random integers between 0 and 255
        # The values are generated using numpy's randint function
        # The dtype is set to uint8 to represent integers in the range [0, 255]
        Ai = np.random.randint(0, 256, size=Ni, dtype=np.uint8)
        
        # Define the filename to save this array, e.g., 'A0.npy'
        # The arrays are saved in the group's subdirectory
        array_filename = os.path.join(group_dir, f'A{array_index}.npy')
        
        # Save the array to a .npy file using numpy's save function
        # This will allow easy loading of the array later using numpy.load()
        np.save(array_filename, Ai)
        
        print(f'Saved array A{array_index} of length {Ni} to {array_filename}')