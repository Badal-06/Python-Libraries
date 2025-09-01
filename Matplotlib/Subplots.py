import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 8, 27, 64, 125]

plt.subplot(2, 1, 1)
plt.plot(x, y1, 'r')
plt.title("Square Numbers")

plt.subplot(2, 1, 2)
plt.plot(x, y2, 'g')
plt.title("Cube Numbers")

plt.tight_layout()
plt.show()