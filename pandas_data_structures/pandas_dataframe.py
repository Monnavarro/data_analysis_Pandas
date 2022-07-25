# -- coding: utf-8 --
"""

Created on: 25/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pandas as pd

df = pd.DataFrame({
    "Name": ["Jane", "John", "Matt", "Ashley"],
    "Age": [24, 21, 26, 32]
})

print(df)

# we check the dimentions of a DataFrame using the shape method that returns a
# tupple cointaining the number of rows and columns.

print(df.shape)
