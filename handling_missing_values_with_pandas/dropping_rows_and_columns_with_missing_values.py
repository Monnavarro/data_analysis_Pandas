# -- coding: utf-8 --
"""

Created on: 3/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "A": [1, 2, 3, np.nan, 7],
    "B": [2.4, np.nan, 5.1, np.nan, 2.6],
    "C": [np.nan, "foo", "zoo", "bar", np.nan],
    "D": [11.5, np.nan, 6.2, 21.1, 8.7],
    "E": [1, 2, 3, 4, 5]
})

print(df)
# Eliminando filas que tienen al menos un valor Nulo en la fila.
print(df.dropna(axis=0, how="any"))

# Eliminando columnas que tienen al menos un valor Nulo en la fila.
print(df.dropna(axis=1, how="any"))


# function THRESH
# Si configuramos el parámetro de thresh en 4, una fila debe tener al
# menos cuatro valores NO NULOS para que no se elimine
print(df)
# Drop rows that have less than 4 non-missing values
print(df.dropna(thresh=4))

# funcion inplace
# Devolviendo un DataFrame después de eliminar las filas que tienen menos
# de cuatro valores que no faltan. Es decir, MODIFICANDO el DataFrame ORIGINAL.

# Sin modificar
print(df)

#Modificando el mismo DataFrame
df.dropna(thresh=4, inplace=True)
print(df)