"""
Generar un reporte gráfico de un Data set (libre elección) 
que como mínimo incluya los siguientes tipos de gráficas: 
plot, bar, area, hist, box, pie, table, scatter, scatter matrix, radViz, 
colormaps (aplicar a cualquier tipo de gráfica).
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./survey_results_public.csv')
print(df.index, df.columns)
print(df)

df = df.cumsum()

plt.figure()
plt.show()

#plt.close("all")
