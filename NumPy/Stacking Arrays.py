import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print("Vertical Stack:\n", np.vstack((a, b)))
print("\nHorizontal Stack:\n", np.hstack((a, b)))