import seaborn as sns
import matplotlib.pyplot as plt

# Load the built-in Iris dataset
data = sns.load_dataset("iris")

# Create a scatter plot
sns.scatterplot(data=data, x="sepal_length", y="petal_length", hue="species", style="species")

# Add title and axis labels
plt.title("Scatter Plot of Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")

# Show the plot
plt.show()