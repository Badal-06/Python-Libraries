# Program 12: Applying functions to columns
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [85, 90, 78]
})

# Add 5 bonus points to each score
df['Score'] = df['Score'].apply(lambda x: x + 5)
print(df)