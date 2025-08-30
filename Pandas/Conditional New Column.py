# Program 20: Creating a new column based on condition
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 60, 95]
})

df['Result'] = df['Score'].apply(lambda x: 'Pass' if x >= 70 else 'Fail')
print(df)