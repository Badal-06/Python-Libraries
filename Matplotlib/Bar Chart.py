import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [20, 35, 30, 35]

plt.bar(categories, values, color='skyblue')
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()