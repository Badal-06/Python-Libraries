# Program 13: Changing column data type
import pandas as pd

df = pd.DataFrame({
    'ID': ['1', '2', '3'],
    'Score': ['85', '90', '88']
})

df['ID'] = df['ID'].astype(int)
df['Score'] = df['Score'].astype(float)
print(df.dtypes)