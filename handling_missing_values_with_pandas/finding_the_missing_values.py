# -- coding: utf-8 --
"""

Created on: 3/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# Encontrando los valores nulo en un Data Frame
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "A": [1, 2, 3, np.nan, 7],
    "B": [2.4, np.nan, 5.1, np.nan, 2.6],
    "C": [np.nan, "foo", "zoo", "bar", np.nan],
    "D": [11.5, np.nan, 6.2, 21.1, 8.7]
})

# función "isna" devuelve TRUE para los valores faltantes
print(df.isna())

"""
       A      B      C      D
0  False  False   True  False
1  False   True  False   True
2  False  False  False  False
3   True   True  False  False
4  False  False   True  False
"""

# Agregando la función sum para contar el numero de nulos en cada columna
print(df.isna().sum())

"""
print(df.isna().sum())
A    1
B    2
C    2
D    1
dtype: int64
"""

# Agregar otra función sum devuelve el núm total de valores faltantes en
# TODO el DataFrame
print(df.isna().sum().sum())

"""
6
"""

# si queremos los valores NULOS que tiene cada FILA, usamos axis=1
print(df.isna().sum(axis=1))
"""
0    1
1    2
2    0
3    2
4    1
dtype: int64
"""

# Función "notna" devuelve FALSE para los valores faltantes
df = pd.DataFrame({
    "A": [1, 2, 3, np.nan, 7],
    "B": [2.4, np.nan, 5.1, np.nan, 2.6],
    "C": [np.nan, "foo", "zoo", "bar", np.nan],
    "D": [11.5, np.nan, 6.2, 21.1, 8.7]
})
print(df.notna())
# Contando número de valores que NO faltan en las columnas
print(df.notna().sum())
"""
       A      B      C      D
0   True   True  False   True
1   True  False   True  False
2   True   True   True   True
3  False  False   True   True
4   True   True  False   True

A    4  --> en la columna A, hay 4 valores NO NULOS.
B    3
C    3
D    4
dtype: int64
"""
