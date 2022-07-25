# -- coding: utf-8 --
"""

Created on: 25/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pandas as pd

myseries = pd.Series(
    [10, 20, 30],
# we can assigned an integer index.
    index = ["a", "b", "c"]
    )

print(myseries)

# we can access the items in a Series with their index.
myseries = pd.Series(
   ["Jane", "John", "Emily", "Matt"]
)

# print the first item
print(myseries[0])


# is_unique method checks for any duplicate item in a Series
myseries = pd.Series([1, 2, 3])
print(myseries.is_unique)

myseries = pd.Series([1, 2, 3, 3, 5])
print(myseries.is_unique)