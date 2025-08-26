import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Add a scalar to all elements
print("Add 10 to all elements:\n", arr + 10)

# Multiply each column by [1, 2, 3]
multiplier = np.array([1, 2, 3])
print("Column-wise multiply:\n", arr * multiplier)