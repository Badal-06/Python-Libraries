import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.set_palette("Set2")
sns.swarmplot(x="day", y="total_bill", data=data)
plt.title("Swarm Plot with Custom Color Palette")
plt.show()