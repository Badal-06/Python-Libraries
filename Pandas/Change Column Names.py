# Program 11: Renaming columns
import pandas as pd

df = pd.DataFrame({
    'fname': ['Alice', 'Bob'],
    'lname': ['Smith', 'Johnson']
})

df.rename(columns={'fname': 'First Name', 'lname': 'Last Name'}, inplace=True)
print(df)