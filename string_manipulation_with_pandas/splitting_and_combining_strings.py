# -- coding: utf-8 --
"""

Created on: 1/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""

import pandas as pd

path = "./string_manipulation_with_pandas/"

staff = pd.read_csv(path + "staff.csv")

# split function (sirve para separar una cadena de caracteres)
print(staff["name"].str.split(" "))

# expand function (sirve para crear una nueva columna después de
# aplicar la función split)
staff["last_name"] = staff["name"].str.split(" ", expand=True)[1]

print(staff[["name", "last_name"]])


# operador "+" (sirve para concatenar cadenas de texto)
print(staff["name"] + " - " + staff["departament"])

