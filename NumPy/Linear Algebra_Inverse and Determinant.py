import numpy as np

matrix = np.array([[1, 2], [3, 4]])

# Determinant
det = np.linalg.det(matrix)
print("Determinant:", det)

# Inverse
inv = np.linalg.inv(matrix)
print("Inverse:\n", inv)