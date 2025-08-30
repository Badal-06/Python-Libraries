# Program 18: Creating time series data
import pandas as pd
import numpy as np

dates = pd.date_range(start='2025-01-01', periods=6, freq='D')
df = pd.DataFrame({'Value': np.random.randint(10, 100, size=6)}, index=dates)
print(df)