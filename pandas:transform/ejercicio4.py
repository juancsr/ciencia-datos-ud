"""
Genere un dataframe donde se almacene el precio (en pesos colombianos) 
de algunos productos a través de los meses de un año. 
A partir del dataframe anterior genere un nuevo dataframe donde los precios de los productos 
se encuentren en dólares, euros y libras.
"""
import numpy as np
import pandas as pd

# Generar dataframe
data = np.random.randint(low=0, high=100, size=(12, 3))
indexes = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
df = pd.DataFrame(data=data, columns=['manzana', 'platano', 'pera'], index=indexes)
print(df)

# dollar
USD = 0.00025834603 # equivalente a 1.00 COP
# euro
EUR = 0.00022120372 # equivalente a 1.00 COP
# libra esterlina
GBP = 0.018959546 # equivalante a 1.00 COP

toUSD = lambda copValue: copValue * USD

def toEUR(copValue):
    return EUR * copValue

def toGBP(copValue):
    return EUR * copValue

# Convirtiendo precios a dololares, euros y libras
df1 = df.transform([toUSD, toEUR, toGBP])
print(df1)