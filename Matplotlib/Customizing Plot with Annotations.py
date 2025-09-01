import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o')
plt.title("Annotated Plot")
plt.xlabel("X")
plt.ylabel("Y")

# Add annotation at the last point
plt.annotate('Prime Number', xy=(5, 11), xytext=(3, 10),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.grid(True)
plt.show()