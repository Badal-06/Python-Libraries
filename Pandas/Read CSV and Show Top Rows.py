# Program 2: Read CSV and display first 5 rows
import pandas as pd

df = pd.read_csv('sample.csv')  # Replace with your CSV file path
print("First 5 rows:\n", df.head())