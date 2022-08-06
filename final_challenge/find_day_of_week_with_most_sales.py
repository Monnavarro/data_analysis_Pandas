# -- coding: utf-8 --
"""

Created on: 5/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pandas as pd

path = "./data_analysis_with_pandas/"

grocery = pd.read_csv(path + "grocery.csv")


def find_day_with_most_sales():
    try:
        grocery["price"] = grocery['price'].fillna(
            grocery.groupby('product_description')['price'].transform('mean')
        )

        grocery["sales_date"] = grocery["sales_date"].astype("datetime64[ns]")
        grocery["day_of_week"] = grocery["sales_date"].dt.dayofweek

        day_with_most_sales = grocery.groupby("day_of_week").agg(
            avg_sales=("sales_quantity", "mean")
        ).sort_values(
            by="avg_sales", ascending=False
        ).index[0]

        return day_with_most_sales
    except:
        pass


print(find_day_with_most_sales())
