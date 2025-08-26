# NumPy: Creating and manipulating arrays
import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])
print("Original array:", arr)

# Create a 2D array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D array:\n", matrix)

# Add 10 to every element
arr_plus_10 = arr + 10
print("\nArray + 10:", arr_plus_10)

# Multiply every element by 2
arr_times_2 = arr * 2
print("\nArray * 2:", arr_times_2)