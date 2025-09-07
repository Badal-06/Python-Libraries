import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("flights")
sns.lineplot(data=data, x="year", y="passengers", hue="month")
plt.title("Line Plot of Flights")
plt.show()