# -- coding: utf-8 --
"""

Created on: 26/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pandas as pd

path = "./creating_a_data_frame/"

sales = pd.read_csv(path + "sales.csv")

# dtypes method returns the data type of all columns.
print(sales.dtypes)

# changing the data type #

# we can return the columns as an Index
print("As Index:")
print(sales.columns)

# we can return the columns in a list
print("As List:")
print(list(sales.columns))

# astype functions change the data types of columns
sales["stock_qty"] = sales["stock_qty"].astype("float")
print(sales.dtypes)

# astype function also accepts a dictionary:
sales = sales.astype({
    "stock_qty": "float",
    "last_week_sales": "float"
})
print(sales.dtypes)