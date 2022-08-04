# -- coding: utf-8 --
"""

Created on: 4/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""

import pandas as pd

path = "./data_analysis_with_pandas/"

grocery = pd.read_csv(path + "grocery.csv")


def find_avg_price():

    grocery["price_category"] = pd.cut(grocery["price"], bins=3,
                                       labels=["cheap", "mid-priced",
                                               "expensive"])
    avg_prices = grocery.groupby("price_category").agg(
      avg_price = ("price", "mean"))

    return list(avg_prices.index), list(avg_prices["avg_price"].round(2))


print(find_avg_price())

"""
(['cheap', 'mid-priced', 'expensive'], [3.36, 6.39, 11.4])
"""