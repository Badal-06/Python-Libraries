import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title("Saving Plot to File")

# Save as PNG
plt.savefig("plot_output.png")

plt.show()