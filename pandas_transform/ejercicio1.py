"""
Crear un ejemplo de pipe con tres funciones. 
La primera y la tercera función deben tener argumentos diferentes al dataframe
"""
import numpy as np
import pandas as pd
import copy
from num2words import num2words

a = np.random.randint(low=0, high=10, size=(3, 3))
df = pd.DataFrame(data=a, columns=['A', 'B', 'C'])

def powColumn(dataframe, col, powValue):
    """(First function) pow all values of one Dataset column

    Args:
        dataframe: dataframe to be updated
        col (str): name of the column
        powValue (int): pow value to be apply into all column values
    
    Returns:
        DataFrame: dataframe updated
    """
    dataframe[col] = dataframe[col]**powValue
    return dataframe


def transpose(dataframe):
    """(Second function) swap beetwen rows and columns

    Args:
        dataframe: dataframe to be updated
    
    Returns:
        DataFrame: dataframe updated
    """
    for i in range(0, len(dataframe.columns)):
        colName = dataframe.columns[i]
        colValue = dataframe.loc[:, colName]
        dataframe.iloc[i] = colValue
    
    return dataframe

def toText(dataframe, row: int=0, col: any=0):
    """Converts one of the dataframe element to text

    Args:
        dataframe (DataFrame): dataframe to be updated
        row (int): the row position
        col (any): the column position

    Returns:
        DataFrame: dataframe updated by the pipe
    """
    if type(col) is int:
        dataframe.iloc[row, col] = num2words(dataframe.iloc[row, col])
    if type(col) is str:
        dataframe.loc[row, col] = num2words(dataframe.loc[row, col])
    return dataframe

def printTitle(text:str):
    """print a text with the next format in console:
        text
        ----

    Args:
        text (str): title value
    """
    print('\n',text)
    print('-'*len(text))
    

printTitle('original')
print(df)
printTitle('after pipes')
print(df.pipe(powColumn,'A',3).pipe(transpose).pipe(toText, 1, 'A'))

# one by one
# printTitle('first pie')
# df.pipe(powColumn,'A',3).pipe(transpose).pipe(toText)
# print(df)
# printTitle('second pipe')
# df.pipe(transpose)
# print(df)
# printTitle('third pipe')
# df.pipe(toText)
# print(df)
