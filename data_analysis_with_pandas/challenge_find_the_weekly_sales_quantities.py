# -- coding: utf-8 --
"""

Created on: 4/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pandas as pd
from pandas import Series

path = "./data_analysis_with_pandas/"

grocery = pd.read_csv(path + "grocery.csv")

grocery["sales_date"] = grocery["sales_date"].astype("datetime64[ns]")

# Encontrar las ventas totales en cada semana y ordenar los resultados por
# ventas totales en orden descendente

def find_weekly_sales():
    try:
        grocery["week"] = Series(grocery["sales_date"].dt.isocalendar().week)
# opción obsoleta muy pronto:
        # grocery["week"] = grocery["sales_date"].dt.week
        result = grocery.groupby("week").agg(
            total_sales=("sales_quantity", "sum")
        ).sort_values(
            by="total_sales",
            ascending=False
        )
        return list(result["total_sales"])
    except:
        pass

print(find_weekly_sales())
"""
print(find_weekly_sales())
[2129, 2047, 2013, 2008, 599]
"""

