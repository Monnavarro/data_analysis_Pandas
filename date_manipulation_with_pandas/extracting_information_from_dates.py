# -- coding: utf-8 --
"""

Created on: 2/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""

import pandas as pd

mydate = pd.to_datetime("2021-10-10")

# desglosando partes de una fecha --ATRIBUTO--
print(f"The year part is: {mydate.year}")
print(f"The month part is: {mydate.month}")
print(f"The week number part is: {mydate.week}")
print(f"The day part is: {mydate.day}")


my_date = pd.to_datetime("2021-12-21- 00:00:00")

# Desglosando más detalles de una fecha --METODO--
print(f"The date part is: {my_date.date()}")
print(f"The day of week is: {mydate.weekday()}")
print(f"The name of the month is: {mydate.month_name()}")
print(f"The name of the day is: {mydate.day_name()}")