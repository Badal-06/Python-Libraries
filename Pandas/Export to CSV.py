# Program 15: Exporting DataFrame to CSV
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Age': [25, 30]
})

df.to_csv('output.csv', index=False)
print("Data exported to output.csv")