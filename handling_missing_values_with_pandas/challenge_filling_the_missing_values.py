# -- coding: utf-8 --
"""

Created on: 3/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "Date": pd.date_range(start="2021-10-01", periods=10),
    "Measurement": [16, 13, 14, 12, np.nan, np.nan, np.nan, 8, 7, 5]
})


def fill_missing_values():
  try:
      df["Measurement"].fillna(method="ffill",limit=2, inplace=True)
      df["Measurement"].fillna(value=df["Measurement"].mean(), inplace=True)
      return list(df["Measurement"])
  except:
    pass

# Data Drame Original
print(df)
"""
        Date  Measurement
0 2021-10-01         16.0
1 2021-10-02         13.0
2 2021-10-03         14.0
3 2021-10-04         12.0
4 2021-10-05          NaN
5 2021-10-06          NaN
6 2021-10-07          NaN
7 2021-10-08          8.0
8 2021-10-09          7.0
9 2021-10-10          5.0
"""
# Modificado
print(fill_missing_values())
"""
[16.0, 13.0, 14.0, 12.0, 12.0, 12.0, 11.0, 8.0, 7.0, 5.0]
"""