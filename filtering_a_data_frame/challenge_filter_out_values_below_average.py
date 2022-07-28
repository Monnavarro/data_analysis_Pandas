# -- coding: utf-8 --
"""

Created on: 28/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""

import pandas as pd

path = "./creating_a_data_frame/"
sales = pd.read_csv(path + "sales.csv")

def find_the_number_of_products():
  average_price = sales["price"].mean() # find the mean value of the
  # price column
  sales_filtered = sales[sales["price"] > average_price] # filter the
  # products that have a price higher than the average price
  number_of_products = sales_filtered["product_code"].nunique()  # find the
  # number of unique product codes in sales_filtered

  return number_of_products

print(find_the_number_of_products())