# -- coding: utf-8 --
"""

Created on: 2/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pandas as pd

path = "./string_manipulation_with_pandas/"

staff = pd.read_csv(path + "staff.csv")

staff = staff.astype({
    "date_of_birth": "datetime64[ns]",
    "start_date": "datetime64[ns]"
})

def find_age():
    try:

        staff["age"] = (staff["start_date"] - staff["date_of_birth"]).dt.days / 365
        staff["age"] = staff["age"].astype("int")
        return list(staff["age"])

    except:
        pass

print(find_age())