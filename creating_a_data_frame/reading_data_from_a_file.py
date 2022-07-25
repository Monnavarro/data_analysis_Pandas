# -- coding: utf-8 --
"""

Created on: 25/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# how to use the read_csv function
import pandas as pd
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

path = "./creating_a_data_frame/"

sales = pd.read_csv(path + "sales.csv")

print(sales.head())


# using usecols parameter #
sales = pd.read_csv(path + "sales.csv", usecols=["product_code", "product_group", "stock_qty"])
print(sales.head())