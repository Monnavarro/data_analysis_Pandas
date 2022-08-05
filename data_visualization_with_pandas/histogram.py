# -- coding: utf-8 --
"""

Created on: 4/8/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import pandas as pd
import matplotlib.pyplot as plt

path = "./data_analysis_with_pandas/"

grocery = pd.read_csv(path + "grocery.csv")

# Histograma de la columna de precios en el supermercado
grocery["price"].plot(kind="hist")

# Para guardar en un carpeta los Gráficos
plt.savefig('./data_visualization_with_pandas/abc.png')

# AJUSTO EL GRAFICO A NUESTRO GUSTO
grocery["price"].plot(
    kind="hist",
    figsize=(10,6),
    title="Histogram of grocery prices",
    xticks=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
)

# Para guardar en un carpeta los Gráficos
plt.savefig('./data_visualization_with_pandas/abc_2.png')