# -- coding: utf-8 --
"""

Created on: 2/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pandas as pd

path = "./string_manipulation_with_pandas/"

staff = pd.read_csv(path + "staff.csv")
# Necesitamos eliminar el signo "$" al principio.
# Necesitamos eliminar el “,” usado como separador de miles
# Necesitamos convertirlo a un formato numérico para hacer cálculos.

def make_salary_proper():
    try:
        staff["salary_cleaned"] = staff["salary"].str[1:].str.replace(",","")
        staff["salary_cleaned"] = staff["salary_cleaned"].astype("int")
        return list(staff["salary_cleaned"])
    except:
        pass

print(make_salary_proper())
