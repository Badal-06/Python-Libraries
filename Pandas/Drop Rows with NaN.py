# Program 16: Dropping rows with missing values
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, np.nan, 90]
})

df.dropna(inplace=True)
print(df)