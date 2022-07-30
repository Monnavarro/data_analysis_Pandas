# -- coding: utf-8 --
"""

Created on: 29/7/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""

import pandas as pd
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

path = "./string_manipulation_with_pandas/"

staff = pd.read_csv(path + "staff.csv")

print(f"\nStaff data frame has the following columns: \n{list(staff.columns)}\n")

print(staff)

# we can get the first letter of the strings in the name column
print(staff["Name"].str[0])
