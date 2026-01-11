import numpy as np

# Create a 1D NumPy array
arr = np.array([10, 20, 30, 40, 50])

# Display array
print("Array:", arr)

# Basic operations
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Reshape into 2x3 matrix (using first 6 elements)
arr2 = np.array([1, 2, 3, 4, 5, 6])
matrix = arr2.reshape(2, 3)

print("Reshaped Matrix:")
print(matrix)
