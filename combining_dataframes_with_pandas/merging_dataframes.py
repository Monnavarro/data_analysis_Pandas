# -- coding: utf-8 --
"""

Created on: 5/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pandas as pd


# Create product and sales DataFrames
product = pd.DataFrame({
    "product_code": [1001, 1002, 1003, 1004],
    "weight": [125, 200, 100, 400],
    "price": [10.5, 24.5, 9.9, 34.5]
})

sales = pd.DataFrame({
    "product_code": [1001, 1002, 1003, 1007],
    "sales_date": ["2021-12-10"] * 4,
    "sales_qty": [8, 14, 22, 7]
})

# Merge DataFrames
merged_df = product.merge(sales, how="left", on="product_code")

print(merged_df)
"""
   product_code  weight  price  sales_date  sales_qty
0          1001     125   10.5  2021-12-10        8.0
1          1002     200   24.5  2021-12-10       14.0
2          1003     100    9.9  2021-12-10       22.0
3          1004     400   34.5         NaN        NaN
"""

## INNER
# create product and sales DataFrames
product = pd.DataFrame({
  "product_code": [1001, 1002, 1003, 1004],
  "weight": [125, 200, 100, 400],
  "price": [10.5, 24.5, 9.9, 34.5]
})

sales = pd.DataFrame({
  "product_code": [1001, 1002, 1003, 1007],
  "sales_date": ["2021-12-10"] * 4,
  "sales_qty": [8, 14, 22, 7]
})

# merge DataFrames
merged_df = product.merge(sales, how="inner", on="product_code")

print(merged_df)
"""
   product_code  weight  price  sales_date  sales_qty
0          1001     125   10.5  2021-12-10          8
1          1002     200   24.5  2021-12-10         14
2          1003     100    9.9  2021-12-10         22
"""

## OUTER
# create product and sales DataFrames
product = pd.DataFrame({
  "product_code": [1001, 1002, 1003, 1004],
  "weight": [125, 200, 100, 400],
  "price": [10.5, 24.5, 9.9, 34.5]
})

sales = pd.DataFrame({
  "product_code": [1001, 1002, 1003, 1007],
  "sales_date": ["2021-12-10"] * 4,
  "sales_qty": [8, 14, 22, 7]
})

# merge DataFrames
merged_df = product.merge(sales, how="outer", on="product_code")

print(merged_df)
"""
   product_code  weight  price  sales_date  sales_qty
0          1001   125.0   10.5  2021-12-10        8.0
1          1002   200.0   24.5  2021-12-10       14.0
2          1003   100.0    9.9  2021-12-10       22.0
3          1004   400.0   34.5         NaN        NaN
4          1007     NaN    NaN  2021-12-10        7.0
"""