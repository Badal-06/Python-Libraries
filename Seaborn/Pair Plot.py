import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("iris")
sns.pairplot(data, hue="species")
plt.suptitle("Pair Plot of Iris Dataset", y=1.02)
plt.show()