# -- coding: utf-8 --
"""

Created on: 2/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pandas as pd

path = "./string_manipulation_with_pandas/"
# create the DataFrame
staff = pd.read_csv(path + "staff.csv")

# Change the data type

staff = staff.astype({
    "date_of_birth": "datetime64[ns]",
    "start_date": "datetime64[ns]"
})

# create raise_date column
# podemos crear una columna llamada fecha_aumento(raise_date)
# agregando un año a la columna fecha_inicio(start_date).
staff["raise_date"] = staff["start_date"] + pd.DateOffset(years=1)

print(staff[["start_date", "raise_date"]].head())


# agrega seis meses a la columna start_date.
staff["start_date"] + pd.DateOffset(months=6)

# Restar horas
mytime = pd.Timestamp("2021-12-14 16:50:00")

print("The first method")
print(mytime + pd.DateOffset(hours=-2))

print("\nThe second method")
print(mytime - pd.DateOffset(hours=2))


# Timedelta function
# agregando 12 semanas a la columna start_date en el staff
# con la función Timedelta.

# add 12 weeks
print(staff["start_date"] + pd.Timedelta(value=12, unit="W"))

# acepta cadenas para especificar la duración que se agregará o restará
# add 12 weeks
print(staff["start_date"] + pd.Timedelta("12 W"))