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

grocery[grocery["product_description"] == "tomato"].plot(
    x="sales_date",
    y=["sales_quantity", "price"],
    kind="line",
    figsize=(10, 5),
    title="Daily tomato sales and prices",
    secondary_y="price"
)

plt.savefig('./data_visualization_with_pandas/graf_multiple_lines.png')
