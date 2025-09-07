import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.displot(data["total_bill"], kde=True)
plt.title("Histogram with KDE - Total Bill")
plt.show()