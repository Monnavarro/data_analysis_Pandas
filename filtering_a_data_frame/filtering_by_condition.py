# -- coding: utf-8 --
"""

Created on: 28/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pandas as pd
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

path = "./creating_a_data_frame/"

sales = pd.read_csv(path + "sales.csv")



# selecciona los productos que pertenecen al grupo de productos PG2.#

sales_filtered = sales[sales.product_group == "PG2"]
print(sales_filtered)
# devuelve lo mismo que la sentencencia de arriba#
print(sales[sales["product_group"] == "PG2"])

# Filtrando un producto mayor a 100 euros
print(sales[sales["price"] > 100])

# Multiple Conditions
sales_filtered = sales[(sales["price"] > 100) & (sales["stock_qty"] < 400)]

print(sales_filtered[["price","stock_qty"]].head())

# imprimiendo los primeros 5 registros de todas las columnas
print(sales_filtered.head())


# Productos que pertenecen al grupo de productos PG1 o PG2.
print(sales[(sales["product_group"] == "PG1") | (sales["product_group"]
                                                 == "PG2")])

# Seleccionar los productos que pertenecen a los grupos de
# productos PG1, PG2 y PG3
print(sales[sales["product_group"].isin(["PG1", "PG2", "PG3"])])

# Los productos que no están en los grupos de productos PG1, PG2 o PG3
print(sales[~sales["product_group"].isin(["PG1", "PG2", "PG3"])])