# Libraries
from keras.layers.normalization.batch_normalization import BatchNormalization
import numpy as np
import os
import re
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

## Original imports
# import keras
# from keras.utils import to_categorical
# from keras.models import Sequential,Input,Model
# from keras.layers import Dense, Dropout, Flatten
# from keras.layers import Conv2D, MaxPooling2D
# from keras.layers.normalization import BatchNormalization
# from keras.layers.advanced_activations import LeakyReLU

# Keras from tensorflow
import tensorflow.keras
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import Input
from tensorflow.keras.models import Sequential,Model
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import LeakyReLU

# Loading images
dirname = os.path.join(os.getcwd(), 'ninhosimages')
print('dirname: {}'.format(dirname))
imgpath = dirname + os.sep

images = []
directories = []
dircount = []
prevRoot = ''
cant = 0

for root, dirnames, filenames in os.walk(imgpath):
    for filename in filenames:
        if re.search("\.(jpg|jpeg|png|bmp|tiff)$", filename):
            cant = cant+1
            filepath = os.path.join(root, filename)
            image = plt.imread(filepath)
            images.append(image)
            b = 'Reading...' + str(cant)
            if prevRoot != root:
                prevRoot = root
                directories.append(root)
                dircount.append(cant)
                cant = 0

dircount.append(cant)

dircount = dircount[1:]
dircount[0] = dircount[0]+1
print('Readed directories: {}'.format(len(directories)))
print('Images per directory: {}'.format(dircount))
print('Total of images: {}'.format(sum(dircount)))

# Making labels and classes
labels = []
indice = 0
for cantidad in dircount:
    for i in range(cantidad):
        labels.append(indice)
    indice = indice+1

print('Number of labels created: {}'.format(len(labels)))
ninhos = []
index = 0
for directory in directories:
    name = directory.split(os.sep)
    print('index, name[len(name)-1]: ', index, name[len(name)-1])
    ninhos.append(name[len(name)-1])
    index = index+1

print(len(images), len(images[0]))
y = np.array(labels)
#convirtiendo de lista a numpy de tipo uint8
X = np.array(images) #convierto de lista a numpy uint8

## Searching unique numbers from the learning labels
classes = np.unique(y)
nClasses = len(classes)
print('Total outputs: {}'.format(nClasses))
print('Output classes: {}'.format(classes))
print(len(X), len(y))
# Mezclar todo y crear los grupos de entrenamiento y testing
train_X, test_X, train_Y, test_Y = train_test_split(X, y, test_size=0.2)
print('Datos de aprendizaje: ', train_X.shape, train_Y.shape)
print('Testing de aprendizaje: ', test_X.shape, test_Y.shape)

plt.figure(figsize=[5,5])

# Display the first image in training data
plt.subplot(121)
plt.imshow(train_X[0], cmap='gray')
plt.title("Ground Truth : {}".format(train_Y[0]))

# Display the first image in testing data
plt.subplot(122)
plt.imshow(test_X[0], cmap='gray')
plt.title("Ground Truth : {}".format(test_Y[0]))

# Iniciar el procesamiento de imagenes