# -- coding: utf-8 --
"""

Created on: 4/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pandas as pd

path = "./data_analysis_with_pandas/"

grocery = pd.read_csv(path + "grocery.csv")

# utilizando AGG para definir un nombre a la columna (promedio del precio)
print(grocery.groupby("product_group").agg(avg_price=("price", "mean")))
"""
               avg_price
product_group           
dairy           8.041176
fruit           3.433333
vegetable       3.266471
"""


# calculando la cantidad de ventas y el precio promedio para cada grupo.
print(grocery.groupby("product_group").agg(
    sales_total=("sales_quantity", "sum"),
    avg_price=("price", "mean")
    ))
"""
               sales_total  avg_price
product_group                        
dairy                 2656   8.041176
fruit                 3558   3.433333
vegetable             2582   3.266471

"""

# función sort_values
# Ordenando las agrupaciones
print(grocery.groupby("product_description").agg(
    total_sales=("price", "mean"),
    avg_price=("sales_quantity", "sum")
    ).sort_values(
        by="total_sales",
        ascending=False
    )
)
"""
                     total_sales  avg_price
product_description                        
butter-0.25kg          11.400000        844
yogurt-1kg              6.693103        882
milk-1L                 6.078571        930
cucumber                4.532857        875
grape                   4.400000        889
plum                    4.389655        883
tomato                  3.121034        845
orange                  2.714286        908
onion                   2.150714        862
apple                   2.077778        878
"""

# AGRUPANDO VARIAS COLUMNAS
print(grocery.groupby(["product_description", "product_group"]).agg(
    sales_total=("sales_quantity", "sum"),
    avg_price=("price", "mean")
))
"""
                                   sales_total  avg_price
product_description product_group                        
apple               fruit                  878   2.077778
butter-0.25kg       dairy                  844  11.400000
cucumber            vegetable              875   4.532857
grape               fruit                  889   4.400000
milk-1L             dairy                  930   6.078571
onion               vegetable              862   2.150714
orange              fruit                  908   2.714286
plum                fruit                  883   4.389655
tomato              vegetable              845   3.121034
yogurt-1kg          dairy                  882   6.693103
"""