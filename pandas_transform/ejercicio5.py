"""
Realice el ejercicio 4 pero únicamente convirtiendo de pesos a dólares (applymap)
"""
import numpy as np
import pandas as pd

# Generar dataframe (igual que en ejercicio 4)
data = np.random.randint(low=0, high=100, size=(12, 3))
indexes = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
df = pd.DataFrame(data=data, columns=['manzana', 'platano', 'pera'], index=indexes)
print(df)

# dollar
USD = 0.00025834603 # equivalente a 1.00 COP
toUSD = lambda copValue: copValue * USD

df1 = df.applymap(toUSD)
print(df1)
