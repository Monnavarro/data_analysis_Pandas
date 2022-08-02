# -- coding: utf-8 --
"""

Created on: 2/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pandas as pd

path = "./string_manipulation_with_pandas/"

staff = pd.read_csv(path + "staff.csv")

# Extraer el estado de la columna ciudad y pasarlas a minúscula

print(staff["city"].str.split(",", expand=True)[1].str.lower())

# otra manera es:
print(staff["city"].str[-2:].str.lower())


# cambiemos la palabra "field quality" a "quality"
print(staff["departament"].str.lower().replace("field quality", "quality"))

# extrae el año de la columna "start_date" y cambia su tipo de datos a entero
print(staff["start_date"].str[:4].astype("int"))

print(staff["start_date"])

# operación de filtrado con la función de query, extrae el año de la
# columna start_date y cambia su tipo de datos a entero.
print(staff.query("name > 'John Doe'").start_date.str[:4].astype("int"))

print(staff)