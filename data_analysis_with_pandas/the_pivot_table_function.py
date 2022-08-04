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

# Creando la columna week
grocery["sales_date"] = grocery["sales_date"].astype("datetime64[ns]")
grocery["week"] = Series(grocery["sales_date"].dt.isocalendar().week)


# Creando una tabla dinámica
print(
    pd.pivot_table(
        data=grocery,
        values="sales_quantity",
        index="product_group",
        columns="week",
        aggfunc="sum"
    )
)
"""
week            44   45   46   47   48
product_group                         
dairy          650  577  597  632  200
fruit          886  819  792  813  248
vegetable      593  617  619  602  151
"""

# Creando tabla dinámica con multiples agregaciones
print(
    pd.pivot_table(
        data = grocery,
        values="price",
        index="week",
        columns="product_group",
        aggfunc=["mean", "std"]
    )
)
"""
                   mean                           std                    
product_group     dairy     fruit vegetable     dairy     fruit vegetable
week                                                                     
44             8.185714  3.403704  3.135000  2.629503  1.134251  0.831913
45             7.750000  3.416000  3.190000  2.158825  1.125344  1.022109
46             7.761111  3.550000  3.420000  2.312406  1.054619  1.069235
47             8.325000  3.396154  3.304286  2.607050  0.933158  1.087789
48             8.400000  3.300000  3.290000  2.720294  0.947176  1.117139
"""

# Mostrar subtotales de columnas y filas y también el total general
print(
    pd.pivot_table(
        data=grocery,
        values="sales_quantity",
        index="product_group",
        columns="week",
        aggfunc="sum",
        margins=True,
        margins_name="Total"
    )
)
"""
week             44    45    46    47   48  Total
product_group                                    
dairy           650   577   597   632  200   2656
fruit           886   819   792   813  248   3558
vegetable       593   617   619   602  151   2582
Total          2129  2013  2008  2047  599   8796
"""