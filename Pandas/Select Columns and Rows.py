# Program 3: Selecting specific columns and rows
import pandas as pd

df = pd.DataFrame({
    'Name': ['Tom', 'Jerry', 'Spike'],
    'Age': [20, 22, 24],
    'Marks': [88, 92, 85]
})

print("Name column:\n", df['Name'])
print("\nFirst two rows:\n", df.iloc[:2])