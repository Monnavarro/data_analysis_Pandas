# -- coding: utf-8 --
"""

Created on: 25/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# Create a data frame by using a Python dictionary.
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Names": ["jane", "John", "Matt", "Ashley"],
    "Ages": [26, 24, 28, 25],
    "Score": [91.2, 94.1, 89.5, 92.3]
})

print(df)

# two-dimensional array
arr = np.random.randint(1, 10, size=(3, 5))

df = pd.DataFrame(arr, columns=["A", "B", "C", "D", "E"])
print(df)