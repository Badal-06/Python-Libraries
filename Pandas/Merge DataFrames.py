# Program 8: Merging two DataFrames
import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 4],
    'Score': [85, 90, 88]
})

merged_df = pd.merge(df1, df2, on='ID', how='inner')
print("Merged DataFrame:\n", merged_df)