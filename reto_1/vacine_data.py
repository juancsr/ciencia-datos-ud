# 1.Se conecte a Datos Abiertos de Colombia para acceder al conjunto de datos de Vacunación de Covid-19 y
# lo convierta en un dataframe de Pandas (Consultar sodapy y socrate).
import os
import pathlib
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from sodapy import Socrata
from flask import Flask, request, send_file

# https://www.datos.gov.co/Salud-y-Protecci-n-Social/Asignaci-n-de-dosis-de-vacuna-contra-COVID-19/sdvb-4x4j
client = Socrata('www.datos.gov.co', None)

results = client.get('sdvb-4x4j', limit=100000)

data = pd.DataFrame.from_records(results)
print(data.columns.values.tolist(),"\n")
app = Flask(__name__)

# cleaning data
data['cantidad'] = pd.to_numeric(data.loc[:,'cantidad'], errors='ignore')

column_names = {
    'num_resolucion': 'Resolución',
    'fecha_resolucion': 'Fecha de Resolucion',
    'a_o': 'Año',
    'cod_territorio': 'Código Territorio',
    'nom_territorio': 'Territorio',
    'laboratorio_vacuna': 'Laboratorio',
    'uso_vacuna': 'Uso Vacuna',
    'fecha_corte': 'Fecha de Corte',
}


@app.route('/territorios')
def territorios():
    frame_data = data['nom_territorio'].drop_duplicates().to_list()
    response = {value: value.replace('_', ' ') for value in frame_data}
    return response


@app.route('/labs')
def labs():
    return data['laboratorio_vacuna'].drop_duplicates().to_dict()


@app.route('/columns')
def columns():
    return column_names


def save_graph(dataframe, gtype) -> str:
    """
    Takes a dataframe, turns into a graph, save the graph as image
        dataframe: dataframe to build the graph
        gtype: kind of plot (same as pandas kind)
    returns the graph image path
    """
    folder_name = 'graphs'
    curr_dict = pathlib.Path(__file__).parent.absolute()
    graph_dict = "{}/{}".format(curr_dict, folder_name)
    columns = dataframe.columns.values.tolist()
    print('columns: ', columns)
    if not os.path.exists(graph_dict):
        os.makedirs(graph_dict)

    filename = "{}_{}.png".format(str(datetime.now()).replace(' ', ''), gtype)
    file_path = "{}/{}".format(graph_dict, filename)

    plot = dataframe.plot(x=columns[0], y=columns[1], kind=gtype, figsize=(20, 10))
    plot.set_xticks(dataframe.index)
    plot.set_xticklabels(dataframe[columns[0]], rotation=90)
    plot.get_figure().savefig(file_path)
    return file_path


def build_graph(xs: str, ys: list, limit=0, asc=True, filter_values=[]) -> str:
    """
    builds the graph image
        x: the x axis
        y: the y axis (can be multiple)
        limit: max number of data to the plot
        asc: asc or desc data
    returns the html table of the dataframe
    """
    if len(filter_values) > 0:
        grouped = data.groupby(xs)[ys].sum().filter(items=filter_values, axis=0)
    else:
        grouped = data.groupby(xs)[ys].sum()
    # frame = dict()
    # for x in xs:
    #     if limit != 0:
    #         upper_limit = limit if asc else data.groupby(x)[ys].count()
    #         lower_limit = upper_limit - limit
            
    #         a = grouped.index.to_list( )[lower_limit:upper_limit]
    #         frame[x] = a
    #         frame['cantidad'] = grouped.loc[a, 'cantidad'].to_list()
    #         #frame = { xs: a, 'cantidad': grouped.loc[a, 'cantidad'].to_list() }
    #     else:
    #         frame[x] = grouped.index.to_list()
    #         frame['cantidad'] = grouped.loc[:,'cantidad'].to_list()
    #         #frame = { xs: grouped.index.to_list(), 'cantidad': grouped.loc[:,'cantidad'].to_list() }

    df = pd.DataFrame(grouped[ys]).fillna(value=0)
    df.sort_values(by=['cantidad'], inplace=True, ascending=not asc)
    upper_limit = limit if limit > 0 else len(df)
    #upper_limit = limit
    #lower_limit = upper_limit - limit
    #print("{} to {}".format(lower_limit, upper_limit))
    indexes = df['cantidad'].index.to_list( )[:upper_limit]
    if not asc:
        indexes.reverse()
    print(indexes)
    print(df.loc[indexes,:])
    return df.loc[indexes,:].to_html()


@app.route('/')
@app.route('/graph')
def graph():
    x = request.args.get('x')
    y = request.args.get('y')
    x = x.replace(' ', '').split(',')
    y = y.replace(' ', '').split(',')
    limit = int(request.args.get('limit'))
    asc = True if request.args.get('order') == 'asc' else False
    filter_values = []
    
    if len(x) == 1 and (x[0] == 'nom_territorio' or x[0] == 'laboratorio_vacuna'):
        if len(request.args.get('filter')) > 0:
            filter_values = request.args.get('filter').split(',')
    
    html = build_graph(x, y, limit, asc, filter_values)
    
    return html


#frame = {'Territorio': data['nom_territorio'], 'Cantidad': data['cantidad'].apply(pd.to_numeric)}
#df = pd.DataFrame(frame).fillna(value=0)
#df['Cantidad'] = df['Cantidad'].apply(pd.to_numeric)
#df.plot(x='Territorio', y='Cantidad', kind='bar', xlim=[0, 10])
# plt.show()
