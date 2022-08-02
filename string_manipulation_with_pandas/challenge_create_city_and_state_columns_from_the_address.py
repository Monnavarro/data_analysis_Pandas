# -- coding: utf-8 --
"""

Created on: 1/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pandas as pd

path = "./string_manipulation_with_pandas/"

staff = pd.read_csv(path + "staff.csv")


# Creando una columna "state" extrayendola de la columna "city"

def create_city_column():
    try:
        staff["state"] = staff["city"].str[-2:]
        return list(staff["state"])
    except:
        pass


print(create_city_column())

#otra solución:
def create_city_column():

  staff["state"] = staff["city"].str.split(",", expand=True)[1]

  return list(staff["state"])


print(create_city_column())
