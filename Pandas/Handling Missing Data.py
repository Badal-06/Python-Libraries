# Program 10: Handling NaN values
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, np.nan, 90]
})

print("Original DataFrame:\n", df)

# Fill NaN with average score
df['Score'].fillna(df['Score'].mean(), inplace=True)

print("\nAfter filling NaN:\n", df)