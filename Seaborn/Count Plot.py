import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("titanic")
sns.countplot(x="class", hue="sex", data=data)

plt.title("Passenger Class Count by Gender")
plt.show()