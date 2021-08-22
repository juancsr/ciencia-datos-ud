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
from pandas.core.frame import DataFrame

df = pd.read_csv('./survey_results_public.csv')
#print(df.index, df.columns)
# print(df)

def save_graph(dataframe, gtype: str, x='', y='', title='') -> str:
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

        # creates folder if doesn't exists
        if not os.path.exists(figures_dict):
            os.makedirs(figures_dict)

        filename = "{}_{}.png".format(str(datetime.now()).replace(' ', '').replace(':', '-'),gtype)
        file_path = "{}/{}".format(figures_dict, filename)
        plot_title = '{}: {}'.format(gtype, x) if title == '' else title
        if gtype == 'scatter': 
            plot = dataframe.plot(x=x, y=y, kind=gtype, figsize=(20, 10))
        elif gtype == 'pie':
            plot = dataframe.plot(x=x, y=y, kind=gtype, figsize=(20, 10))
        else:
            if y != '':
                print('y is not empty')
                plot = dataframe.fillna(value=0).plot(kind=gtype, xlabel=x, ylabel=y, y=y,  x=x, title=plot_title, figsize=(20, 10))
            else:
                plot = dataframe[x].fillna(value=0).plot(kind=gtype, xlabel='People', ylabel=x, title=plot_title, figsize=(20, 10))

        plot.get_figure().savefig(file_path)
        return file_path
    except Exception as e:
        print('error saving graph ({}) -> {}'.format(gtype, e))


lower_limit = 0
upper_limit = 100

print(df.columns)

ages = df['Age']
main_branch = df['MainBranch']
age_1st_code = df['Age1stCode']
country = df['Country']
database_next_year = df['DatabaseDesireNextYear']
web_framework = df['WebframeWorkedWith']

frame = {'MainBranch': main_branch, 'Age1stCode': age_1st_code, 'Age': ages, 
'Country': country, 'DatabaseNextYear': database_next_year, 'WebFramework': web_framework}
n_df = DataFrame(frame).fillna(value=0).reset_index()

# only takes the first 100 records, i don't want a gigant plot
reduced_df = DataFrame(n_df[lower_limit: upper_limit])

# groupped dataframes
grouped_by_country = reduced_df.groupby('Country').aggregate(np.sum)

# plot line
line_path = save_graph(reduced_df, 'line', 'Age', title='Devs by Age')

# bar
country_df = DataFrame({'Country ': grouped_by_country.index, 'People': grouped_by_country['Age']}).reset_index()
line_path = save_graph(country_df.loc[:, ('Country', 'People')], 'bar', 'Country', 'People', 'Devs by Country')

# area
area_path = save_graph(country_df.loc[:, ('Country', 'People')], 'area', 'Country', 'People', 'Devs by Country')

# hist
grouped_by_webframework = reduced_df.groupby(by='WebFramework').aggregate(np.sum).reset_index()
grouped_by_webframework.rename(columns = {'index': 'People'}, inplace=True)

plot = reduced_df.fillna(value=0).plot(kind='hist', 
    xlabel='Frameworks', ylabel='Popularity', 
    x='WebFramework', title='Framework popularity', figsize=(20, 10))
plot.get_figure().savefig('./figures/hist.png')


# pie
grouped_by_database = reduced_df.groupby(['DatabaseNextYear']).sum().dropna(axis=0, how='any')
grouped_by_database = grouped_by_database.loc['Cassandra;DynamoDB;MongoDB':]
print(grouped_by_database)
plot_pie = grouped_by_database.plot(kind='pie', y='index', title='Database to learn next year per dev', figsize=(20, 20), autopct='%1.1f%%')
plot_pie.get_figure().savefig('./figures/pie.png')

# # box
# box_path = save_graph(reduced_df, 'box', 'Age1stCode', 'MainBranch', title='First time coding')
# # dfbox = df[lower_limit:upper_limit].fillna(value=0)
# # print(dfbox)
# # file_path = save_graph(dfbox, 'box')

# # pie
# pie_path = save_graph(reduced_df, 'pie', 'DatabaseDesireNextYear', title='Desired database for next year')

# print(reduced_df.columns)
# # scatter
# scatter_path = save_graph(reduced_df, 'scatter', 'DatabaseDesireNextYear', title='Desired database for next year')
