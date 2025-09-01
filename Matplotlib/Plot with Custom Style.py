import matplotlib.pyplot as plt

plt.style.use('ggplot') 

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker='D', linewidth=2)
plt.title("Styled Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()