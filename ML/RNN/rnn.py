import os
import sys
import numpy as np
np.random.seed(5)

from keras.layers import Input, Dense, SimpleRNN
from keras.models import Model
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.utils import to_categorical
from keras import backend as K


# 1. LECTURA DEL SET DE DATOS
# ===========================================================
# JC: Abre el fichero en modo lectura y almacena su contenido
nombres = open(os.path.join(sys.path[0], 'nombres_dinosaurios.txt'),'r').read()
# JC: cada caracter del fichero se pone en minuscula
nombres = nombres.lower()

# Crear diccionario (listado de caracteres que no se repiten)
# JC: Crea una lista con los caracteres y simbolos (\n o \t) del contenido del fichero
alfabeto = list(set(nombres))
# JC: Calcula el tamaño del string de nombres y de la lista con los caracteres
tam_datos, tam_alfabeto = len(nombres), len(alfabeto)
# JC: Imprime la información anterior
print("En total hay %d caracteres, y el diccionario tiene un tamaño de %d caracteres." % (tam_datos, tam_alfabeto))

# Conversión de caracteres a índices y viceversa
# JC: Crea un diccionario por comprensión primero organizando el alfabeto y luego asignandole valores consecutivos con enumerate
car_a_ind = { car:ind for ind,car in enumerate(sorted(alfabeto))}
# JC: Crea un diccionario utilizando los indices como llave y el caracter como valor de la llave
ind_a_car = { ind:car for ind,car in enumerate(sorted(alfabeto))}
# JC: Imprime los dos diccionarios anteriores
print(car_a_ind)
print(ind_a_car)

# 2. MODELO
# ===========================================================
n_a = 25    # Número de unidades en la capa oculta
# JC: Entrada de la red neuronal, tod
entrada  = Input(shape=(None,tam_alfabeto))
# JC: Estado inicial de la red neuronal. El estado oculto
a0 = Input(shape=(n_a,))
# JC: Celda recurrente para el entrenamiento. 25 Neurona, a la salida nos retorna le nuevo estado actualizado
celda_recurrente = SimpleRNN(n_a, activation='tanh', return_state = True)
# JC: Capa de salida con el tama;o y la función de activación. Toma la celda recurrente para su activación
capa_salida = Dense(tam_alfabeto, activation='softmax')
# JC: La salida esperada es la activación generada por la celda recurrente
salida = []
# JC: Se realiza una instancia de la celda recurrente utilizando la entrada (lista) y el estado inicial de esa entrada (valores)
hs, _ = celda_recurrente(entrada, initial_state=a0)
# JC: La salida se instancia agregando el resultado de la caelda de recurrencia a la capa de salida
salida.append(capa_salida(hs))
# JC: Se crea el modelo utilizando la entrada de datos, su estado oculto y la salida espeda
modelo = Model([entrada,a0],salida)
modelo.summary()
# JC: Se crea el optimizador gradiente descendiente para el entrentamiento del modelo. Aqui se crea el optimizador
opt = SGD(lr=0.0005)
# JC: Aqui se agrega.
modelo.compile(optimizer=opt, loss='categorical_crossentropy')


# 3. EJEMPLOS DE ENTRENAMIENTO
# ===========================================================

# Crear lista con ejemplos de entrenamiento y mezclarla aleatoriamente
with open(os.path.join(sys.path[0], 'nombres_dinosaurios.txt')) as f:
    ejemplos = f.readlines()
# JC: Crea una lista por comprension utilizando los nombes de dinosaurios
ejemplos = [x.lower().strip() for x in ejemplos]
# JC: Re organiza aletaroreamente los nombres de los dinosaurios
np.random.shuffle(ejemplos)

# Crear ejemplos de entrenamiento usando un generador
def train_generator():
    while True:
        # Tomar un ejemplo aleatorio
        ejemplo = ejemplos[np.random.randint(0,len(ejemplos))]

        # Convertir el ejemplo a representación numérica
        X = [None] + [car_a_ind[c] for c in ejemplo]

        # Crear "Y", resultado de desplazar "X" un caracter a la derecha
        Y = X[1:] + [car_a_ind['\n']]

        # Representar "X" y "Y" en formato one-hot
        x = np.zeros((len(X),1,tam_alfabeto))
        # JC: organiza los onehot con base en el tama;o del alfabeto
        onehot = to_categorical(X[1:],tam_alfabeto).reshape(len(X)-1,1,tam_alfabeto)
        x[1:,:,:] = onehot
        y = to_categorical(Y,tam_alfabeto).reshape(len(X),tam_alfabeto)

        # Activación inicial (matriz de ceros)
        a = np.zeros((len(X), n_a))

        yield [x, a], y

# 4. ENTRENAMIENTO
# ===========================================================
BATCH_SIZE = 80			# Número de ejemplos de entrenamiento a usar en cada iteración
NITS = 10000			# Número de iteraciones

for j in range(NITS):
    # JC: Ajustar el modelo utilizando los ejemplos de entranmiento establecidos anteriormente
    historia = modelo.fit_generator(train_generator(), steps_per_epoch=BATCH_SIZE, epochs=1, verbose=0)

    # Imprimir evolución del entrenamiento cada 1000 iteraciones
    if j%1000 == 0:
        print('\nIteración: %d, Error: %f' % (j, historia.history['loss'][0]) + '\n')


# 5. GENERACIÓN DE NOMBRES USANDO EL MODELO ENTRENADO
# ===========================================================
def generar_nombre(modelo,car_a_num,tam_alfabeto,n_a):
    ''' JC
    generar_modelo
    --------------
    params:
        modelo: modelo a usar
        car_a_num: mapeo de caracterest
        tam_alfabeto: tamanio del alfabeto
        n_a: capa oculta de entrada
    '''
    # Inicializar x y a con ceros
    x = np.zeros((1,1,tam_alfabeto,))
    a = np.zeros((1, n_a))

    # Nombre generado y caracter de fin de linea
    nombre_generado = ''
    fin_linea = '\n' # JC: caracter que representa una nueva linea
    car = -1 # JC: Fin

    # Iterar sobre el modelo y generar predicción hasta tanto no se alcance
    # "fin_linea" o el nombre generado llegue a los 50 caracteres
    contador = 0
    while (car != fin_linea and contador != 50):
          # Generar predicción usando la celda RNN
          a, _ = celda_recurrente(K.constant(x), initial_state=K.constant(a))
          y = capa_salida(a)
          prediccion = K.eval(y)

          # Escoger aleatoriamente un elemento de la predicción (el elemento con
          # con probabilidad más alta tendrá más opciones de ser seleccionado)
          # JC: Escoge alaetoreamente un elemento de una prediccion
          ix = np.random.choice(list(range(tam_alfabeto)),p=prediccion.ravel())

          # Convertir el elemento seleccionado a caracter y añadirlo al nombre generado
          car = ind_a_car[ix]
          # JC: Contactena el nombre generado con el caracter encontrado
          nombre_generado += car

          # Crear x_(t+1) = y_t, y a_t = a_(t-1)
          x = to_categorical(ix,tam_alfabeto).reshape(1,1,tam_alfabeto)
          a = K.eval(a)

          # Actualizar contador y continuar
          contador += 1

          # Agregar fin de línea al nombre generado en caso de tener más de 50 caracteres
          if (contador == 50):
            nombre_generado += '\n'

    print(nombre_generado)

# Generar 100 ejemplos de nombres generados por el modelo ya entrenado
for i in range(100):
    generar_nombre(modelo,car_a_ind,tam_alfabeto,n_a)