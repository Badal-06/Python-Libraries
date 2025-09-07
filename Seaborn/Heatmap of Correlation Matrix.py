import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("iris")

# Select only numeric columns
numeric_data = data.select_dtypes(include='number')
corr = numeric_data.corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap - Iris Dataset")
plt.show()