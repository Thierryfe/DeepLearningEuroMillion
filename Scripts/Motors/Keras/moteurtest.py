
from __future__ import print_function
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import backend as K
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

last=Dense(62, activation='sigmoid')
model.add(last)
#model.compile(loss='binary_crossentropy',
#optimizer='rmsprop',
#metrics=['accuracy'])

model.compile(loss='binary_crossentropy',
optimizer='rmsprop',)

certes=model.fit(M,tabresultat,
epochs=6,
batch_size=128)

print(certes)
test_y=np.asarray([[1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]])
K.backend.__get__(last)
test_x=np.asarray([[1,8,11,25,28,4,6]])
print(type(test_x)," ou ",Y[-1])
score = model.evaluate(test_x, test_y)

ynew = model.predict_classes(test_x)

for i in range(0,len(ynew)):
	print("vaux ",ynew[i])
model.summary()
#sprint(score)



import matplotlib.pyplot as plt

#from Modules import Parsing

data1 = csvtotabforkeras(2004, 2020)

colors = ("red", "green", "blue", "yellow", "violet", "orange", "black")
groups = ("n1", "n2", "n3", "n4", "n5", "s1", "s2")

x = [[1,2,3,4,5,6,7] for i in range(len(data1))]



def scatter_plot(listes,y):
    groups = ("n")

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(y, listes, alpha=0.8, s=30, label=groups)

    plt.title('Matplot scatter plot')
    plt.legend(loc=2)
    plt.show()

inp = model.input                                           # input placeholder
outputs = [layer.output for layer in model.layers]          # all layer outputs
functors = [K.function([inp, K.learning_phase()], [out]) for out in outputs]    # evaluation functions

# Testing
#test = np.random.random(7)[np.newaxis,...]
layer_outs = [func([test_x, 1.]) for func in functors]
lll=layer_outs[1]

lll=np.asarray(lll)
print (" FALOOOOO ",lll)


scatter_plot(tabresultat,tabresultat)
tf.keras.backend.clear_session

