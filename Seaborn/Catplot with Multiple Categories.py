import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
sns.catplot(x="day", y="total_bill", hue="sex", col="time", kind="box", data=data)
plt.suptitle("Catplot - Box Plots by Time, Day, and Sex", y=1.05)
plt.show()