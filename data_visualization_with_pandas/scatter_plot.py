# -- coding: utf-8 --
"""

Created on: 5/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import matplotlib.pyplot as plt
import pandas as pd

path = "./creating_a_data_frame/"

sales = pd.read_csv(path + "sales.csv")

print(sales[["product_code", "product_group", "price", "cost"]].head())
"""
   product_code product_group    price    cost
0          4187           PG2   569.91  420.76
1          4195           PG2   712.41  545.64
2          4204           PG2   854.91  640.42
3          4219           PG2  1034.55  869.69
4          4718           PG2    26.59   12.54
"""

# Dispersión
sales.plot(
    x="price",
    y="cost",
    kind="scatter",
    figsize=(8, 5),
    title="Cost vs Price"
)

plt.savefig('./data_visualization_with_pandas/graf_dispersion.png')

# ajustando datos atipicos
sales.plot(
    x="price",
    y="cost",
    kind="scatter",
    figsize=(8, 5),
    title="Cost vs Price",
    xlim=(0, 1000),
    ylim=(0, 800),
    grid=True
)

plt.savefig('./data_visualization_with_pandas/graf_dispersion_2.png')