import pandas as pd

# Creating a Series from a list
data_list = [10, 20, 30, 40, 50]
series_from_list = pd.Series(data_list)
print("Series from list:")
print(series_from_list)

# Creating a Series from a dictionary
data_dict = {'a': 100, 'b': 200, 'c': 300}
series_from_dict = pd.Series(data_dict)
print("\nSeries from dictionary:")
print(series_from_dict)

# Creating a Series with custom index
custom_index_series = pd.Series([1, 2, 3], index=['x', 'y', 'z'])
print("\nSeries with custom index:")
print(custom_index_series)
