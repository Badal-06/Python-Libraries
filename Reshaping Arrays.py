# NumPy: Reshaping arrays
import numpy as np

arr = np.arange(1, 13)  # Create array from 1 to 12
print("Original array:", arr)

# Reshape into 3x4
reshaped = arr.reshape(3, 4)
print("\nReshaped to 3x4:\n", reshaped)

# Flatten back to 1D
flattened = reshaped.flatten()
print("\nFlattened array:", flattened)