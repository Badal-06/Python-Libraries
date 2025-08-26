# NumPy: Array Slicing
import numpy as np

# Create a 1D array
arr = np.array([10, 20, 30, 40, 50, 60, 70])
print("Original Array:", arr)

# Slice from index 1 to 4 (elements at index 1, 2, 3)
print("Slice arr[1:4]:", arr[1:4])

# Slice from the beginning to index 3 (not including index 3)
print("Slice arr[:3]:", arr[:3])

# Slice from index 3 to the end
print("Slice arr[3:]:", arr[3:])

# Slice with a step of 2
print("Slice arr[::2]:", arr[::2])

# Reverse the array using slicing
print("Reversed Array:", arr[::-1])

# Create a 2D array for slicing
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("\n2D Array:\n", matrix)

# Slice first two rows and first two columns
print("Sliced 2D Array (first 2 rows & columns):\n", matrix[:2, :2])

# Get the second column from all rows
print("Second column:", matrix[:, 1])

# Get the last row
print("Last row:", matrix[-1, :])