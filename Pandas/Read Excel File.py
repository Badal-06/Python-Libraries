# Program 14: Reading Excel file
import pandas as pd

# Requires: pip install openpyxl
df = pd.read_excel('sample.xlsx')
print(df.head())