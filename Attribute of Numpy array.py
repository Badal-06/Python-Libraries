# NumPy: Array Attributes
import numpy as np

# Create a 2D NumPy array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("Array:\n", arr)

# Shape of the array (rows, columns)
print("\nShape:", arr.shape)

# Number of dimensions
print("Dimensions:", arr.ndim)

# Total number of elements
print("Size:", arr.size)

# Data type of elements
print("Data type:", arr.dtype)

# Item size in bytes
print("Item size (bytes):", arr.itemsize)

# Total bytes consumed by the elements
print("Total bytes consumed:", arr.nbytes)

# Transpose of the array
print("Transpose:\n", arr.T)