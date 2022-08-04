# -- coding: utf-8 --
"""

Created on: 3/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pandas as pd
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)
# pd.set_option('display.max_rows', 500)

path = "./data_analysis_with_pandas/"

grocery = pd.read_csv(path + "grocery.csv")

print("The size of the DataFrame:")
print(grocery.shape)
"""
The size of the DataFrame:
(300, 7)
"""

print("\nThe column names are:")
print(list(grocery.columns))
"""
The column names are:
['product_code', 'product_description', 'product_group', 'sales_date', 
'price', 'sales_quantity', 'unit']
"""

print(("\nThe first five rows"))
print(grocery.head())
"""
The first five rows
   product_code product_description product_group  sales_date  price  sales_quantity unit
0          1001              tomato     vegetable  2021-11-01   2.99              36   kg
1          1001              tomato     vegetable  2021-11-02   2.99              23   kg
2          1001              tomato     vegetable  2021-11-03   2.99              34   kg
3          1001              tomato     vegetable  2021-11-04   2.99              23   kg
4          1001              tomato     vegetable  2021-11-05   2.99              34   kg
"""

# Función GROUPBY
# Agrupando por "product_group" el promedio del archivo grocery
print(grocery.groupby("product_group").mean())
"""
               product_code     price  sales_quantity
product_group                                        
dairy                1202.0  8.041176       29.511111
fruit                1102.5  3.433333       29.650000
vegetable            1002.0  3.266471       28.688889
"""

# Agrupando solo las columnas seleccionadas.
print(grocery[["product_group", "price"]].groupby("product_group").mean())
"""
                  price
product_group          
dairy          8.041176
fruit          3.433333
vegetable      3.266471
"""
# Redondeando la columna PRICe a 2 decimales:
print(round(grocery[["product_group", "price"]].groupby("product_group").mean(), 2))
"""
               price
product_group       
dairy           8.04
fruit           3.43
vegetable       3.27
"""