
from __future__ import print_function
import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten

import SetDataForKeras
from SetDataForKeras import csvtotabforkeras
import numpy as np
from KerasSetResultat import KerasSetResultat

import pandas as pnd

#---------------------------------------------
# PREPARATION DES DONNEES
#---------------------------------------------
Y=csvtotabforkeras(2004,2019);

print(Y)

#---------------------------------------------
# CREATION DES JEUX D'APPRENTISSAGE ET DE TEST
#---------------------------------------------

#Creation des jeux d'apprentissage
#from sklearn.model_selection import train_test_split
#train_x, test_x, train_y, test_y = train_test_split(X, Y, test_size=0.20, random_state=42)

# Génération de données aléatoires
#x_train = np.random.random((1000, 20))
#y_train = np.random.randint(2, size=(1000, 1))
#x_test = np.random.random((100, 20))

tabresultat=KerasSetResultat(Y)

M=np.delete(Y, (-1), axis=0)

model = Sequential()
model.add(Dense(64, input_dim=7, activation='relu'))

model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(62, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
optimizer='rmsprop',
metrics=['accuracy'])

certes=model.fit(M,tabresultat,
epochs=6,
batch_size=128)

print(certes)
test_y=np.asarray([[1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
test_x=np.asarray([[1,8,11,25,28,4,6]])
print(type(test_x)," ou ",Y[-1])
score = model.evaluate(test_x, test_y)
#sprint(score)
tf.keras.backend.clear_session

