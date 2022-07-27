# -- coding: utf-8 --
"""

Created on: 26/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pandas as pd

path = "./creating_a_data_frame/"

sales = pd.read_csv(path + "sales.csv")

# nunique function returns the number of distinct values in a column
print(sales["product_group"].nunique())

#  unique function shows the unique values.
print(sales["product_group"].unique())


# value_counts function return all the distinct values in a column
# along with the number of their occurrences.
print(sales["product_group"].value_counts())