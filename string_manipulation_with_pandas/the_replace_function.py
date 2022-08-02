# -- coding: utf-8 --
"""

Created on: 1/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""

import pandas as pd

path = "./string_manipulation_with_pandas/"

staff = pd.read_csv(path + "staff.csv")

# Reemplazar una "," por " -" con la función replace
print(staff["city"].str.replace(",", " -"))

# creando una columna "state"
staff["state"] = staff["city"].str[-2:]
print(staff["state"])

# Reemplazando la abreviatura del estado por los nombres
staff["state"].replace(
    {"TX":"Texas", "CA": "California", "FL": "Florida", "GA": "Georgia"},
    inplace=True
)
print(staff["state"])