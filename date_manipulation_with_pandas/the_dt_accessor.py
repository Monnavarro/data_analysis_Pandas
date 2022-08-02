# -- coding: utf-8 --
"""

Created on: 2/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""

import pandas as pd

path = "./string_manipulation_with_pandas/"

staff = pd.read_csv(path + "staff.csv")

# cambiando el tipo de datos de las columnas
staff = staff.astype({
    "date_of_birth": "datetime64[ns]",
    "start_date": "datetime64[ns]"
})

# creando la columna start_month
staff["start_month"] = staff["start_date"].dt.month

print(staff[["start_date", "start_month"]])

# Devuelve un DataFrame que contiene la información del año, la semana del
# calendario y el día de la semana
staff["start_date"].dt.isocalendar().year