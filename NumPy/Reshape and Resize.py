import numpy as np

arr = np.arange(1, 13)
reshaped = arr.reshape(4, 3)
print("Reshaped Array:\n", reshaped)

# Resize modifies original array
Resized=np.resize(arr, (3, 5))
print("\nResized Array:\n", Resized)