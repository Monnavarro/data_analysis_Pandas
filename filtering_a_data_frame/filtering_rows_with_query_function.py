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

# seleccionar productos con un precio superior a 100
print(sales.query("price > 100"))

# Multiple Conditions
print(sales.query("price > 100 and stock_qty < 400").head())

# seleccionar los productos que pertenecen al grupo de productos, PG2
print(sales.query("product_group == 'PG2'").head())