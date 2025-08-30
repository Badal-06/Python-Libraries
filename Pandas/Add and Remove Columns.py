# Program 6: Adding and removing columns
import pandas as pd

df = pd.DataFrame({
    'Name': ['Tom', 'Jerry', 'Spike'],
    'Marks': [88, 92, 85]
})

df['Grade'] = ['B', 'A', 'B']  # Add column
df.drop('Marks', axis=1, inplace=True)  # Remove column

print("Updated DataFrame:\n", df)