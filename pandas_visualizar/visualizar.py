"""
Generar un reporte gráfico de un Data set (libre elección) 
que como mínimo incluya los siguientes tipos de gráficas: 
☑ plot, 
☑ bar, 
☑ area, 
☑ hist, 
☑ box, 
☑ pie, 
table, 
☑ scatter, 
scatter matrix, 
radViz, 
colormaps (aplicar a cualquier tipo de gráfica).
"""
import os
import pathlib
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

df = pd.read_csv('./survey_results_public.csv')
#print(df.index, df.columns)
print(df)

def save_graph(dataframe, gtype: str) -> str:
    try:
        """
        Takes a dataframe, turns into a graph, save the graph as image
            dataframe: dataframe to build the graph
            gtype: kind of plot (same as pandas kind)
        returns the graph image path
        """
        folder_name = 'figures'
        curr_dict = pathlib.Path(__file__).parent.absolute()
        figures_dict = "{}/{}/{}".format(curr_dict, folder_name, gtype)
        columns = dataframe.columns.values.tolist()
        if not os.path.exists(figures_dict):
            os.makedirs(figures_dict)

        filename = "{}_{}.png".format(str(datetime.now()).replace(' ', '').replace(':', '-'),gtype)
        file_path = "{}/{}".format(figures_dict, filename)

        if gtype == 'scatter': 
            plot = dataframe.plot(x=columns[0], y=columns[2], kind=gtype, figsize=(20, 10))
        elif gtype == 'pie':
            plot = dataframe.plot(x=columns[0], y=columns[3], kind=gtype, figsize=(20, 10))
        else:
            plot = dataframe.plot(x=columns[8], y=columns[4], kind=gtype)
        plot.set_xticks(dataframe.index)
        plot.set_xticklabels(dataframe[columns[0]], rotation=90)
        plot.get_figure().savefig(file_path)
        return file_path
    except Exception as e:
        print('error saving graph {}'.format(e))

lower_limit = 0
upper_limit = 50

dfline = df[lower_limit:upper_limit].fillna(value=0)
print(dfline)
file_path = save_graph(dfline, 'line')

dfbar = df[lower_limit:upper_limit].fillna(value=0)
print(dfbar)
file_path = save_graph(dfbar, 'bar')


dfarea = df[lower_limit:upper_limit].fillna(value=0)
print(dfarea)
file_path = save_graph(dfarea, 'area')

dfhist = df[lower_limit:upper_limit].fillna(value=0)
print(dfhist)
file_path = save_graph(dfhist, 'hist')

dfbox = df[lower_limit:upper_limit].fillna(value=0)
print(dfbox)
file_path = save_graph(dfbox, 'box')

dfpie = df[lower_limit:upper_limit].fillna(value=0)
print(dfpie)
file_path = save_graph(dfpie, 'pie')

dfscatter = df[lower_limit:upper_limit].fillna(value=0)
print(dfscatter)
file_path = save_graph(dfscatter, 'scatter')

#plt.figure()
#plt.show()

#plt.close("all")
