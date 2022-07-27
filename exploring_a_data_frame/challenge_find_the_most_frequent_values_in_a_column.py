# -- coding: utf-8 --
"""

Created on: 27/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# we’ll find the three most frequent values in a column by using the
# functions and methods that we’ve learned so far. The find_most_frequents
# function below is designed to find the three most frequent values (in order)
# of the given column in the sales.

import pandas as pd

path = "/Users/mon/PycharmProjects/data_analysis_pandas/creating_a_data_frame/"

sales = pd.read_csv(path + "sales.csv")


def find_most_frequents(column_name):
    try:
        return list(sales[column_name].value_counts().index[0:3])
    except:
        pass

print(f"column: last_week_sales {find_most_frequents('last_week_sales')}")
print(f"column: product_group {find_most_frequents('product_group')}")
print(f"column: product_code {find_most_frequents('product_code')}")
