# -- coding: utf-8 --
"""

Created on: 28/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import numpy as np
import pandas as pd

path = "./creating_a_data_frame/"

sales = pd.read_csv(path + "sales.csv")

# primeras 5 registros de dos columnas (Método loc) #
print(sales.loc[:4, ["product_code", "product_group"]])

# Método iloc #
print(sales.iloc[[5, 6, 7, 8], [0, 1]])
print(sales.iloc[5:9, :2])

# creando indíces y columnas con el método loc #
df = pd.DataFrame(
     np.random.randint(10, size=(4,4)),
     index = ["a", "b", "c", "d"],
     columns = ["col_a", "col_b", "col_c", "col_d"]
     )

print(df)

print("\nSelect two rows and two columns using loc:")
print(df.loc[["a", "b"], ["col_a", "col_b"]])

print("\nSelect two rows and two columns using iloc:")
print(df.iloc[:2])








