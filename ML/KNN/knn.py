'''
1. Seleccionar 2 conjunto de datos de atributos numéricos de UCI, con características diferentes 
    (# de atributos, # de muestras, tipo de dato, descripción estadística, etc...) 
    de tal forma que permitan obtener conclusiones válidas 
    al evaluar el desempeño de KNN en función de las características del conjunto de datos.
2. Hacer un análisis estadístico descriptivo de los conjuntos de datos.
3. Evaluar KNN (únicamente mediante score()) para cada conjunto de datos, 
    para diferentes valores de K.
4. Obtener conclusiones sobre la relación del desempeño de KNN con respecto 
    a las características del conjunto de datos.
5. Generar recomendaciones referentes a la selección 
    del hiperparámetro K en función de las características del conjunto de datos.
'''

import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import statistics as st

## 1. Seleccionar 2 conjunto de datos de atributos numéricos de UCI
def runClassifier(df: pd.DataFrame, k: int) -> None:
    df
    df.replace('?',0, inplace=True)
    x_train, x_test, y_train, y_test = train_test_split(df.iloc[:,:20], df.iloc[:,10:11])
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train.values.ravel()) 
    print("k: {} -> {}".format(k, knn.score(x_test, y_test)))

## first dataset
df1 = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data')
print(df1)
## second dataset
df2 = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/lung-cancer/lung-cancer.data')
print(df2)

# 2. Hacer un análisis estadístico descriptivo de los conjuntos de datos.
print("--- Statistics ---")
print("**** Mean ****")
print(df1.mean())
print("**** Median ****")
print(df1.median())
print("**** Median grouped ****")
print(st.median_grouped(df1.iloc[2]))
print("**** Mode ****")
print(df1.mode())

print("*** Varianza ***")
print(st.pvariance(df2.iloc[2]))
print(st.variance(df2.iloc[2]))
print("*** Desv. estandar ***")
print(df2.std())

# 3. Evaluar KNN (únicamente mediante score()) para cada conjunto de datos, 
# para diferentes valores de K.
print("----- FIRST DATASET ------")
for i in range(1, 21):
    runClassifier(df1, i)

print("----- SECOND DATASET ------")
for i in range(1, 21):
    runClassifier(df2, i)

# 4. Obtener conclusiones sobre la relación del desempeño de KNN 
# con respecto a las características del conjunto de datos.
'''
- En general, los mejores valores de KNN se obtienen cuando k esta dentro del rango de 5 a 9 para ambos dataset
- El primer dataset tiene muchos mas datos y en general sus resultados fueron mejores que el segundo.
- Con valores muy similares, KNN parece no diferencia entre vecinos (es decir, 0.98 no se diferencia mucho de 0.97 o 0.96).
'''

# 5. Generar recomendaciones referentes a la selección del hiperparámetro K en función de 
# las características del conjunto de datos.
'''
- Los valores posteriores a k=9 varian, pero en general se puede decir que la presición disminuye
- Los datos enteros del segundo dataset presentan mayor variedad a los resultados de KNN
'''