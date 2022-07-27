# -- coding: utf-8 --
"""

Created on: 26/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pandas as pd

path = "./creating_a_data_frame/"

sales = pd.read_csv(path + "sales.csv")

# shape method returns a tuple that contains the number of rows and columns
print(sales.shape)

# size method constains a number that shows the number of rows
# multiplied by the number of columns. Returns the total number of cells
# in a DataFrame.
print(sales.size)

# len function give us the number of rows in a DataFrame
print(len(sales))