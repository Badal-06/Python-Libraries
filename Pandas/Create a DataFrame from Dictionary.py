# Program 1: Create a DataFrame from dictionary
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Delhi', 'Mumbai', 'Bangalore']
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)