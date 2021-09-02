'''
Seleccionar 4 distribuciones de https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator, 
graficar el histograma para varias configuraciones de los parámetros de cada distribución seleccionada (similar al ejemplo mostrado a continuación), 
de tal forma que se puedan sacar conclusiones sobre el efecto de esos parámetros.
'''
import numpy as np
from matplotlib import pyplot as plt
from numpy.random import Generator, PCG64

rng = np.random.default_rng()

# size of numbers for each plot
length = 100
plt.figure(figsize=(16, 16))

# 1: Enteros
a = [3, 2, 3]
b = [6, 10, 99]
for i in range(0, len(a)):
    int = rng.integers(a[i], b[i], length)
    plt.subplot(4, 3, i+1).set_title('Integer ({}); a={}; b={}'.format(i+1, a[i], b[i]))
    plt.hist(int)

# 2 normal
a = [-0.3, 2, 3]
b = [.4, 10, 6]
for i in range(0, len(a)):
    norm = rng.normal(a[i], b[i], length)
    plt.subplot(4, 3, i+4).set_title('Normal ({}); a={}; b={}'.format(i+1, a[i], b[i]))
    plt.hist(norm)

# # 3 Exponencial
a = [24, 30, 36]
for i in range(0, len(a)):
    exp = rng.exponential(a[i], length)
    plt.subplot(4, 3, i+7).set_title('Exponencial ({}); scale={}'.format(i+1, a[i]))
    plt.hist(exp)

# 4 Poisson
a = [6, 30, 50]
l = [10, 40, 70] # lenghts
for i in range(0, len(a)):
    poiss = rng.poisson(a[i], l[i])
    print(poiss)
    plt.subplot(4, 3, i+10).set_title('Poisson ({}); events={}'.format(i+1, l[i]))
    plt.hist(poiss)

plt.savefig(fname='./hist.png')

# conclusiones
'''
1. El histograma utilizando el valores normales tiene forma de función campana de Gauss
2. El histograma de exponencial siempre va disminuyendo sus valores (de esperarse por la potencia que se aplica a e) 
3. Poisson es bastante común que no existan valores dentro de los parámetros cuando la cantidad de datos es menor
'''
