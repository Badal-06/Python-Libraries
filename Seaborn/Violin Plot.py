import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.violinplot(x="day", y="total_bill", hue="sex", data=data, split=True)
plt.title("Violin Plot of Total Bill by Day and Sex")
plt.show()