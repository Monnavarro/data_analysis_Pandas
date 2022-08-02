# -- coding: utf-8 --
"""

Created on: 2/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pandas as pd

path = "./string_manipulation_with_pandas/"

staff = pd.read_csv(path + "staff.csv")

# Podemos convertir una cadena que representa una fecha en una marca
# de tiempo usando el constructor to_datetime
my_date = pd.to_datetime("2021-11-10")

print(my_date)

# representar la diferencia entre dos objetos de fecha y hora.
first_date = pd.to_datetime("2021-10-10")
second_date = pd.to_datetime("2021-10-02")

diff = first_date - second_date

print(diff)

# Los objetos Timedelta tienen un atributo de días que devuelve
# el número de días como un número entero.
first_date = pd.to_datetime("2021-10-10")
second_date = pd.to_datetime("2021-10-02")

diff = first_date - second_date

print(type(diff))
print("\n")
print(diff.days)

#cambiando el tipo de dato a fecha
staff = staff.astype({
    "date_of_birth": "datetime64[ns]",
    "start_date": "datetime64[ns]"
})
print(staff.dtypes)