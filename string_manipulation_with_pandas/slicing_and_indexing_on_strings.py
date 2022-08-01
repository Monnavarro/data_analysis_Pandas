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
print(staff["name"].str[0])

# select the first three letters of the name column
print(staff["name"].str[0:3])

# we can star without zero
print(staff["name"].str[:3])

# The following line of code returns the last two characters
# of the city column.
print(staff["city"].str[-2:])

#  we can create a slice that involves every other character, starting
#  from the second-to-last index.
print(staff["name"].str[1::2])