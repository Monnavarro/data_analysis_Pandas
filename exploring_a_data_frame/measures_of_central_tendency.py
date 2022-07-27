# -- coding: utf-8 --
"""

Created on: 27/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""

import pandas as pd

myseries = pd.Series([1, 2, 5, 7, 11, 36])

# median of a series
print(myseries.median())

# mode of a serie
myseries = pd.Series([1, 4, 6, 6, 6, 11, 11, 24])

print(f"The mode of my series is {myseries.mode()[0]}")


# exercise sales
path = "./creating_a_data_frame/"

sales = pd.read_csv(path + "sales.csv")

print("mean:")
print(sales["price"].mean())

print("median:")
print(sales["price"].median())

print("mode:")
print(sales["price"].mode()[0])

print("minimum:")
print(sales["price"].min())

print("maximum:")
print(sales["price"].max())


# variance and Standard deviation
print("Variance:")
print(sales["price"].var())

print("Standard Deviation")
print(sales["price"].std())