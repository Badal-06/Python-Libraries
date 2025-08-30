# Program 4: Filtering rows based on condition
import pandas as pd

df = pd.DataFrame({
    'Name': ['Tom', 'Jerry', 'Spike', 'Tyke'],
    'Age': [20, 22, 24, 18]
})

filtered_df = df[df['Age'] > 20]
print("Filtered Data:\n", filtered_df)