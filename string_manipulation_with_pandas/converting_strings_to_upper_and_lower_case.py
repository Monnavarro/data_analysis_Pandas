# -- coding: utf-8 --
"""

Created on: 1/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""

import pandas as pd

path = "./string_manipulation_with_pandas"

staff = pd.read_csv(path + "staff.csv")

# función lower (convertir los nombres de una columnas a minúsculas)
staff["name_lower"] = staff["name"].str.lower()

print(staff[["name", "name_lower"]])

# función capitalize (convierte la primer letra en mayúscula de una cadena)
print(staff["departament"].str.capitalize())


# función upper (convierte toda la cadena a mayúsculas)
print(staff["departament"].str.upper())

# imprimiendo solo el primer registro de la columna departament
print(staff["departament"][0].upper())