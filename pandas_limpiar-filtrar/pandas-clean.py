"""
Nom: Juan Camilo Sarmiento Reyes
Cod: 20152020067
"""
import os
import numpy as np
import pandas as pd

def title(text):
    print("*** {} ***".format(text.upper()))

""" 
1. Importar uyn CSV desde Datos Abiertos
url: https://www.datos.gov.co/en/Ciencia-Tecnolog-a-e-Innovaci-n/Software-P-blico-Colombia-hist-rico-de-proyectos-p/dubk-bq6v
"""
csv_path = os.path.abspath("pandas:limpiar-filtrar/Software_P_blico_Colombia__hist_rico_de_proyectos_publicados.csv")
df = pd.read_csv(csv_path)
print(df)

"""
2. Limpiar datos
Utilizar cada uno de los métodos de limpieza mostrados a continuación y comentar su efecto. 
"""
title("Limpiar datos")

"""
- df.isnull()
Muestra un valor booleano True cuando el valor de la celda está vacio (NaN).
Si el valor no es un NaN la celda se muestra en False
"""
#print(df.isnull())

"""
- df.dropna(axis=0, how='any')
Con axis=0 elimina las filas
Con how='any' Elimina la fila en donde algún elemento de la misma tenga un valor nulo, bien sea toda la fila o una columna de esa fila 
"""
#print(df.dropna(axis=0, how='any'))

"""
- df.dropna(axis=0, how='all')
Con axis=0 elimina las filas
Con how='all' Si todos los valores de la fila son NaN, elimina esa fila
"""
#print(df.dropna(axis=0,how='all'))


"""
- df.dropna(axis=1, how='any')
Con axis=1 elimina las columnas
Con how='any' si una fila tiene un valor NaN en alguna de sus columnas, elimina esa columna
"""
# Aquí el data frame va a quedar empty porque todas sus filas tienen un NaN en al menos una de sus columnas
#print(df.dropna(axis=1, how='any')) 

"""
- df.fillna(value=3)
Asigna el valor de 'value' a las celdas vacias (NA/NaN) del dataframe
value puede ser un escalar, un diccionario, una serie o un dataframe
"""
#print(df.fillna(value=3))

"""
- df.fillna(df.mean())
df.mean(): Obtiene el valor de la media del dataframe completo
dt.mean(axis=1, numeric_only=True)
    axis=1 usa únicamente las columnas
    numeric_only=true Incluye unicamente las columnas que tengan valores flotantes, interos y booleanos
"""
#print(df.mean(1, numeric_only=True))
#df.fillna(df.mean(axis=1,numeric_only=True))
#print(df.loc[:,['Año del proyecto']])

"""
- df.fillna(method='bfill', limit=1)
    method='bfill' Usa el siguiente valor valido en la secunencia y llena la celda (en este dataset se puede observar la diferencia en el segundo element)
    limit=1 (máximo número de valores consecutivos que va a llenar la función)
"""
#print(df.fillna(method='bfill', limit=1))

"""
3. Filtrado y consulta de datos
Utilizar cada uno de los filtros mostrados a continuación y comentar su efecto.
"""
title("Filtrado y consulta de datos")

"""
df['columna n’] >= valor
¿Qué retorna?
Es un filtro que retorna una serie con valores de True si la condición se cumple y de lo contrario False
"""
# print(type(df['Año del proyecto'] >= '2015'))
# print(df['Año del proyecto'] >= '2015')

"""
df[df['columna n'] >= valor]
¿Qué retorna?
Es un filtro que retorna un dataframe con los valores que cumplan con la condición dada
"""
# print(type(df[df['Año del proyecto'] >= '2015']))
# print(df[df['Año del proyecto'] >= '2015'])

"""
df['columna n'][df['columna m'] >= valor]
¿Qué retorna?
Primero trae los datos hasta la columna n, luego filtra los resultados de los datos con la columna especificada (m)
Retorna un serie
"""
#print(type(df['Organización'][df['Año del proyecto'] >= '2018']))
#print(df['Organización'][df['Año del proyecto'] >= '2018'])

"""
df[(df['columna n'] >= valor) & (df['columna m] >= valor)]
¿Qué retorna?
Retorna un dataframe en el que se cumplen las dos condiciones
"""
#print(type(df[(df['Versión'] >= '3.0') & (df['Año del proyecto'] >= '2017')]))
#print(df[(df['Versión'] >= '1.0') & (df['Año del proyecto'] >= '2017')])

"""
Where
Mask

- ¿Cuál es la principal diferencia entre where y mask?
En where los que NO cumplen la condición se reemplazan con Nan, con mask, lo que SÍ la cumplen se reemplazan con NaN.

- ¿El relleno solo se puede hacer con NaN?
No, el segundo parámetro se puede recibe el valor que se quiere asignar tanto con where, como con mask.

- ¿Qué otras opciones de relleno existen?
Escalar,  serie, dataframe o una función
"""
#print(df.where(df.loc[:,'Nombre del proyecto'] == 'Sofware Público'))
#print(df.mask(df == df.iloc[0]))

"""
Isin

¿Cuál es la diferencia de pasarle como parámetro una lista o un diccionario? 
Con una lista va a poner en True todos los valores en las celdas que coincidan con elementos de la lista
Con un diccionario va a poner en True todos los valores de las celdas cuyas columnas coincidan con el nombre de la llave del diccionario
"""
#print(df.isin(["Software Público",1]))
#print(df.isin({"Nombre del proyecto": ["Software Público", "Civic Software"]}).iloc[0:7,:])

"""
Query
Eval

¿Cuál es la principal diferencia entre Query y Eval?
Query: Consulta las columnas del data frame con expresiones booleanas
Eval: Evalua una expresión de python como un string (+, -, *, /, **, %, | (or), & (and), ~(not)), 
el resultado es True si se cumple la condición, de lo contrario es False
"""
#print(df.query('`URL` == `URL Código`'))
#print(df.eval("URL == `URL Código`"))