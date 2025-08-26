import numpy as np

arr = np.arange(1, 11)

# Randomly choose 5 elements
print("Random Choice:", np.random.choice(arr, 5, replace=False))

# Shuffle array in place
np.random.shuffle(arr)
print("Shuffled Array:", arr)