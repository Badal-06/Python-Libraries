import numpy as np

arr = np.arange(1, 10)

print("Split into 3 parts:", np.split(arr, 3))
print("Vertical Split:\n", np.vsplit(np.arange(1, 13).reshape(3, 4), 3))