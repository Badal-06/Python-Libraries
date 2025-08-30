# Program 17: Creating a multi-level index
import pandas as pd

arrays = [
    ['Group1', 'Group1', 'Group2', 'Group2'],
    ['A', 'B', 'A', 'B']
]
index = pd.MultiIndex.from_arrays(arrays, names=('Group', 'Subgroup'))

df = pd.DataFrame({'Data': [10, 20, 30, 40]}, index=index)
print(df)