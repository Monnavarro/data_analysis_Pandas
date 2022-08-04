# -- coding: utf-8 --
"""

Created on: 4/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pandas as pd

# Creando una serie con valores del 0 al 10
A = pd.Series([5, 0, 2, 8, 4, 10, 7])

# Función de corte "cut"
A_binned = pd.cut(A, bins=4)

print(A_binned)
"""
0      (2.5, 5.0]
1    (-0.01, 2.5]
2    (-0.01, 2.5]
3     (7.5, 10.0]
4      (2.5, 5.0]
5     (7.5, 10.0]
6      (5.0, 7.5]
dtype: category
Categories (4, interval[float64, right]): [(-0.01, 2.5] < (2.5, 5.0]
 < (5.0, 7.5] < (7.5, 10.0]]
"""


# Creando tres contenedores

# Creando una serie con valores del 0 al 10
A = pd.Series([5, 0, 2, 8, 4, 10, 7])

# Función de corte "cut" CONTENEDORES MANUALES
A_binned = pd.cut(A, bins=[-1, 3, 6, 10], labels=["small", "medium", "large"])

print(A_binned)
"""
0    medium
1     small
2     small
3     large
4    medium
5     large
6     large
dtype: category
Categories (3, object): ['small' < 'medium' < 'large']
"""
print("\n")
print(A_binned.value_counts())
"""
large     3
small     2
medium    2
dtype: int64
"""

# Función "qcut" --> agrupa los valores en contenedores para que
# haya aproximadamente el mismo número de valores en cada contenedor.

# Creando una serie
A = pd.Series([1, 4, 2, 10, 5, 6, 8])

# Función "qcut"
A_binned = pd.qcut(A, q=3)

print(A_binned.value_counts())
"""
(0.999, 4.0]    3
(4.0, 6.0]      2
(6.0, 10.0]     2
dtype: int64
"""

# Passing a list to the "q" parameter

# creando una serie
A = pd.Series([1, 4, 2, 10, 5, 6, 8])

# The qcut function
A = pd.Series([1, 4, 2, 3, 10, 5, 6, 8, 7, 5, 9, 14])

A_binned = pd.qcut(A, q=[0, 0.50, 0.75, 1])

print(A_binned.value_counts())

"""
(0.999, 5.5]    6
(5.5, 8.25]     3
(8.25, 14.0]    3
dtype: int64

"""


