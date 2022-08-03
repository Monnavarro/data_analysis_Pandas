# -- coding: utf-8 --
"""

Created on: 3/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pandas as pd
import numpy as np

#representando valores faltantes

df = pd.DataFrame({
    "A": [1, 2, 3, np.nan],
    "B": [2.4, 6.2, 5.1, np.nan],
    "C": ["foo", "zoo", "bar", np.nan]
})

print(df)

#mirando el tipode datos de cada columna
print(df.dtypes)


# Convirtiendo los valores de la columna "A" a enteros:
df["A"] = df["A"].astype(pd.Int64Dtype())

print(df)
print(df.dtypes)