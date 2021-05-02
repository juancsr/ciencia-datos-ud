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

results = client.get('sdvb-4x4j',limit=100000)

data = pd.DataFrame.from_records(results)

app = Flask(__name__)


@app.route('/territorios')
def territorios():
    frame_data = data['nom_territorio'].drop_duplicates().to_list()
    response = {value: value.replace('_',' ') for value in frame_data}
    return response

@app.route('/labs')
def labs():
    return data['laboratorio_vacuna'].drop_duplicates().to_dict()


def save_graph(dataframe, gtype='line') -> str:
    """
    Takes a dataframe, turns into a graph, save the graph as image
        dataframe: dataframe to build the graph
        gtype: kind of plot (same as pandas kind)
    returns the graph image path
    """
    folder_name = 'graphs'
    curr_dict = pathlib.Path(__file__).parent.absolute()
    graph_dict = "{}/{}".format(curr_dict, folder_name)

    if not os.path.exists(graph_dict):
        os.makedirs(graph_dict)

    filename = "{}_{}.png".format(str(datetime.now()).replace(' ',''), gtype)
    file_path = "{}/{}".format(graph_dict, filename)

    dataframe.plot(x='x', y='cantidad', kind=gtype).get_figure().savefig(file_path)
    return file_path


def build_graph(x: str, ys: list, limit=0, asc=True, *args, **kwargs) -> str:
    """
    builds the graph image
        x: the x axis
        y: the y axis (can be multiple)
        limit: max number of data to the plot
        asc: asc or desc data
    returns the path of the plot's image
    """
    print(limit, asc)
    upper_limit = limit - 1 if asc else data[x].count()
    lower_limit = upper_limit - limit

    print('{} to {}'.format(lower_limit, upper_limit))

    x = { 'x': data.loc[lower_limit:upper_limit, x] }
    y = { y: pd.to_numeric(data.loc[lower_limit:upper_limit, y], errors='ignore') for y in ys }
    frame = dict(x, **y)
    df = pd.DataFrame(frame).fillna(value=0)
    fig_path = save_graph(df)
    return fig_path


@app.route('/')
@app.route('/graph')
def graph():
    query_args = request.args.get('nom_territorio')
    limit = int(request.args.get('limit'))
    order = request.args.get('order') if request.args.get else 'asc'
    #for arg in query_args:
        #print(request.args.get(arg))
    asc = True if order == 'asc' else False
    img_path = build_graph('nom_territorio', ['cantidad'], limit, asc)
    print(img_path)
    return send_file(img_path, mimetype='image/png')



#frame = {'Territorio': data['nom_territorio'], 'Cantidad': data['cantidad'].apply(pd.to_numeric)}
#df = pd.DataFrame(frame).fillna(value=0)
#df['Cantidad'] = df['Cantidad'].apply(pd.to_numeric)
#df.plot(x='Territorio', y='Cantidad', kind='bar', xlim=[0, 10])
#plt.show()
