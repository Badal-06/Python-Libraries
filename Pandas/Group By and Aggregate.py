# Program 7: Grouping and aggregating data
import pandas as pd

df = pd.DataFrame({
    'City': ['Delhi', 'Mumbai', 'Delhi', 'Bangalore'],
    'Sales': [100, 150, 200, 130]
})

grouped_sales = df.groupby('City')['Sales'].sum()
print("Total Sales by City:\n", grouped_sales)