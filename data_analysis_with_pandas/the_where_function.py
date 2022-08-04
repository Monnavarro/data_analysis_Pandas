# -- coding: utf-8 --
"""

Created on: 4/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pandas as pd

path = "./data_analysis_with_pandas/"

grocery = pd.read_csv(path + "grocery.csv")

grocery["price_updated"] = grocery["price"].where(
    grocery["price"] >= 3,
    other=grocery["price"] * 1.1
)

print("Checking prices less than $3:")
print(grocery[grocery["price"] < 3][["price", "price_updated"]].head())
"""
Checking prices less than $3:
   price  price_updated
0   2.99          3.289
1   2.99          3.289
2   2.99          3.289
3   2.99          3.289
4   2.99          3.289
"""

print("\nChecking prices of $3 or more:")
print(grocery[grocery["price"] >= 3][["price", "price_updated"]].head())
"""
Checking prices of $3 or more:
    price  price_updated
14   3.49           3.49
15   3.49           3.49
16   3.49           3.49
17   3.49           3.49
18   3.49           3.49

"""


#### OTRO EJEMPLO CON WHERE

grocery["price_updated"] = grocery["price"].where(
  grocery["product_group"] != "vegetable",
  other=grocery["price"] * 0.9
)

print("Checking prices of vegetables:")
print(grocery[grocery["product_group"] == "vegetable"][["price","price_updated"]].head())
"""
Checking prices of vegetables:
   price  price_updated
0   2.99          2.691
1   2.99          2.691
2   2.99          2.691
3   2.99          2.691
4   2.99          2.691
"""

print("\nChecking prices of other products:")
print(grocery[grocery["product_group"] != "vegetable"][["price","price_updated"]].head())
"""
Checking prices of other products:
    price  price_updated
90    4.5            4.5
91    4.5            4.5
92    4.5            4.5
93    4.5            4.5
94    4.5            4.5
"""