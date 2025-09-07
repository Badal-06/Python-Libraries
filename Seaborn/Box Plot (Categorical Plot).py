import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", data=data)
plt.title("Box Plot of Total Bill by Day")
plt.show()