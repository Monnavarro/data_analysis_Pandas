# -- coding: utf-8 --
"""

Created on: 3/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import  pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": [1, 2, 3, np.nan, 7],
    "B": [2.4, np.nan, 5.1, np.nan, 2.6],
    "C": [np.nan, "foo", "zoo", "bar", np.nan],
    "D": [11.5, np.nan, 6.2, 21.1, 8.7],
    "E": [1, 2, 3, 4, 5]
})

# funcion fillna
# Reemplazando los valores nulos de la columna A con el promedio
# de los registros que si tienen datos.
print(df["A"].fillna(value=df["A"].mean()))
"""
0    1.00
1    2.00
2    3.00
3    3.25
4    7.00
Name: A, dtype: float64

"""

# reemplazando el valor en varias columnas
print(df)
"""
Date frame Original
     A    B    C     D  E
0  1.0  2.4  NaN  11.5  1
1  2.0  NaN  foo   NaN  2
2  3.0  5.1  zoo   6.2  3
3  NaN  NaN  bar  21.1  4
4  7.0  2.6  NaN   8.7  5
"""
# Primero definiremos los valores a reemplazar en las columnas
value_a = df["A"].mean()
value_d = df["D"].mean()

# Reemplazando los valores NULOS
print(df.fillna({"A": value_a, "D": value_d}))
"""
      A    B    C       D  E
0  1.00  2.4  NaN  11.500  1
1  2.00  NaN  foo  11.875  2
2  3.00  5.1  zoo   6.200  3
3  3.25  NaN  bar  21.100  4
4  7.00  2.6  NaN   8.700  5
"""

# dataframe ORIGINAL
print(df)
"""
Date frame Original
     A    B    C     D  E
0  1.0  2.4  NaN  11.5  1
1  2.0  NaN  foo   NaN  2
2  3.0  5.1  zoo   6.2  3
3  NaN  NaN  bar  21.1  4
4  7.0  2.6  NaN   8.7  5
"""
## method = “bfill”: Reemplazar valores faltantes hacia atrás, lo que
# significa que un valor faltante se reemplaza por el valor que viene después.
print("Filling backward")
print(df["A"].fillna(method="bfill"))
"""
Filling backward (hacia atrás)
0    1.0
1    2.0
2    3.0
3    7.0
4    7.0
Name: A, dtype: float64
"""

## method = “ffill”: Reemplazar los valores que faltan hacia adelante,
# lo que significa que un valor que falta se reemplaza por el valor que
# viene antes.
print("Filling forward")
print(df["A"].fillna(method="ffill"))
"""
Filling forward (delante)
0    1.0
1    2.0
2    3.0
3    3.0
4    7.0
Name: A, dtype: float64
"""

# Parámetro limit
# Podemos limitar la cantidad de valores que faltan para completar
# con el reemplazo hacia adelante y hacia atrás.

df = pd.DataFrame({
    "A": [1, 2, np.nan, np.nan, 8]
})

print(df)

print("Without the limit parameter")
print(df.fillna(method="bfill"))
"""
Without the limit parameter
     A
0  1.0
1  2.0
2  8.0
3  8.0
4  8.0
"""

print("\nWith the limit parameter")
print(df.fillna(method="bfill", limit=1))
"""
With the limit parameter
     A
0  1.0
1  2.0
2  NaN
3  8.0
4  8.0

"""


