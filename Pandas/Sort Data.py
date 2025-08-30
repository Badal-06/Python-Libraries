# Program 5: Sorting a DataFrame
import pandas as pd

df = pd.DataFrame({
    'Name': ['Tom', 'Jerry', 'Spike'],
    'Marks': [88, 92, 85]
})

sorted_df = df.sort_values(by='Marks', ascending=False)
print("Sorted Data:\n", sorted_df)