import matplotlib.pyplot as plt
import numpy as np

# Generate random data for three groups
np.random.seed(0)
group_A = np.random.normal(70, 10, 100)  # Mean=70, SD=10, 100 samples
group_B = np.random.normal(60, 15, 100)
group_C = np.random.normal(75, 5, 100)

# Combine data into a list
data = [group_A, group_B, group_C]

# Create box plot
plt.boxplot(data, labels=['Group A', 'Group B', 'Group C'], patch_artist=True)

# Add title and axis labels
plt.title("Box Plot of Three Groups")
plt.ylabel("Scores")
plt.grid(True)

plt.show()