# NumPy: Random number generation
import numpy as np

# Random integers between 1 and 10
rand_ints = np.random.randint(1, 11, size=5)
print("Random integers:", rand_ints)

# Random floats between 0 and 1
rand_floats = np.random.rand(5)
print("Random floats:", rand_floats)

# Random normal distribution (mean=0, std=1)
rand_norm = np.random.randn(5)
print("Random normal values:", rand_norm)