# Program 9: Creating a pivot table
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'Bob'],
    'Subject': ['Math', 'Math', 'Science', 'Science'],
    'Score': [90, 85, 88, 92]
})

pivot = pd.pivot_table(df, values='Score', index='Name', columns='Subject')
print("Pivot Table:\n", pivot)