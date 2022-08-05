# -- coding: utf-8 --
"""

Created on: 5/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""

import pandas as pd

df1 = pd.DataFrame({"A": [1, 5, 3, 2], "B":[11, 6, 9, 6],
                    "C": ["a", "d", "f", "b"]})

df2 = pd.DataFrame({"A": [2, 4, 1, 7],"B": [14, 9, 5, 8],
                    "C": ["b", "b", "j", "a"]})

# Combinando dos DataFrames con la función "CONCAT"
df_combined = pd.concat([df1, df2], axis=0)

print(df_combined)

"""
   A   B  C
0  1  11  a
1  5   6  d
2  3   9  f
3  2   6  b
0  2  14  b
1  4   9  b
2  1   5  j
3  7   8  a
"""

# Combinanado dos Dataframes con columnas distintas (ignore_index)
df1 = pd.DataFrame({"A": [1, 5, 3, 2], "B": [11, 6, 9, 6],
                    "C":["a", "d", "f", "b"]})

df2 = pd.DataFrame({"A": [2, 4, 1, 7], "B": [14, 9, 5, 8],
                    "D": ["b", "b", "j", "a"]})

df_combined = pd.concat([df1, df2], axis=0, ignore_index=True)

print(df_combined)
"""
   A   B    C    D
0  1  11    a  NaN
1  5   6    d  NaN
2  3   9    f  NaN
3  2   6    b  NaN
4  2  14  NaN    b
5  4   9  NaN    b
6  1   5  NaN    j
7  7   8  NaN    a
"""

# Uniendo dos tablas en una sola.
df1 = pd.DataFrame({"A": [1, 5, 3, 2], "B": [11, 6, 9, 6],
                    "C":["a", "d", "f", "b"]})

df2 = pd.DataFrame({"A": [2, 4, 1, 7], "B": [14, 9, 5, 8],
                    "D": ["b", "b", "j", "a"]})


df_combined = pd.concat([df1, df2], axis=1)

print(df_combined)
"""
   A   B  C  A   B  D
0  1  11  a  2  14  b
1  5   6  d  4   9  b
2  3   9  f  1   5  j
3  2   6  b  7   8  a
"""

# DataFrames con diferentes indices
df1 = pd.DataFrame({"A": [1, 5, 3, 2], "B": [11, 6, 9, 6],
                    "C": ["a", "d", "f", "b"]})

df2 = pd.DataFrame({"A": [2, 4, 1, 7], "B": [14, 9, 5, 8],
                    "D": ["b", "b", "j", "a"]},
                   index=[3, 4, 5, 6])

df_combined = pd.concat([df1, df2], axis=1)

print(df_combined)
"""
     A     B    C    A     B    D
0  1.0  11.0    a  NaN   NaN  NaN
1  5.0   6.0    d  NaN   NaN  NaN
2  3.0   9.0    f  NaN   NaN  NaN
3  2.0   6.0    b  2.0  14.0    b
4  NaN   NaN  NaN  4.0   9.0    b
5  NaN   NaN  NaN  1.0   5.0    j
6  NaN   NaN  NaN  7.0   8.0    a
"""
