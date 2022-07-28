# -- coding: utf-8 --
"""

Created on: 28/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pandas as pd

path = "./creating_a_data_frame/"

sales = pd.read_csv(path + "sales.csv")

selected_columns = ["product_code", "price"]

# asignandole a la variable selected_columns una lista de las columnas
print(sales[selected_columns].head())

# añadiendo directamente el nombre de las columnas en una lista
print(sales[["product_code", "price"]].head())
