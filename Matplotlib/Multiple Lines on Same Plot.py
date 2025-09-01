import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 25, 30, 50]
y2 = [5, 15, 20, 35, 45]

plt.plot(x, y1, label="Line 1", marker='o')
plt.plot(x, y2, label="Line 2", linestyle='--', marker='x')
plt.title("Multiple Lines")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()