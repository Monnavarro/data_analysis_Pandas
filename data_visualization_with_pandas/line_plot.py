# -- coding: utf-8 --
"""

Created on: 5/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pandas as pd
import matplotlib.pyplot as plt

path = "./data_analysis_with_pandas/"

grocery = pd.read_csv(path + "grocery.csv")

# Ventas diarias de tomates en el supermercado
grocery[grocery["product_description"] == "tomato"].plot(
    x="sales_date",
    y="sales_quantity",
    kind="line",
    figsize=(10, 5),
    title="Daily tomato sales",
    #xlabel="sales date",
    #ylable="sales quantity"
)

plt.savefig('./data_visualization_with_pandas/graf_line.png')
