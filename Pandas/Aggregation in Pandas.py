import pandas as pd

# Creating a DataFrame
data = {
    'Department': ['HR', 'HR', 'IT', 'IT', 'Finance', 'Finance'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'Salary': [50000, 55000, 60000, 62000, 58000, 60000]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Aggregation: Mean salary per department
mean_salary = df.groupby('Department')['Salary'].mean()
print("\nMean Salary per Department:")
print(mean_salary)

# Aggregation: Sum and count per department
agg_result = df.groupby('Department').agg({
    'Salary': ['sum', 'count', 'max', 'min']
})
print("\nAggregation (sum, count, max, min) per Department:")
print(agg_result)