from __future__ import print_function
import tensorflow as tf
from tensorflow.keras import Model
from tensorflow import keras
from tensorflow.keras import backend as K
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
import Scripts.Modules.KerasSetResultat as sr
import Scripts.Modules.saveAndDisplayResultKeras as sa
import Scripts.Modules.SetDataForKeras as sd

import numpy as np
def NetworkCNN(Nb_Epoch,date1,date2):
# ---------------------------------------------
# Récupération des Données
# ---------------------------------------------
    Y = sd.SetDataForKeras(date1, date2);
# ---------------------------------------------
# CREATION DES JEUX D'APPRENTISSAGE ET DE TEST
# ---------------------------------------------

    tabresultat = sr.KerasSetResultat(Y)
    layer_name = "numero"
    W = [Y[-1]]
    M = np.delete(Y, (-1), axis=0)

    model = Sequential()
    model.add(Dense(89, input_dim=7, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(78, activation='relu'))
    model.add(Dropout(0.5))

    last = Dense(62, activation='sigmoid',name=layer_name)
    model.add(last)

    model.compile(loss='binary_crossentropy',
              optimizer='rmsprop', )

    model.fit(M, tabresultat,
                   epochs=Nb_Epoch,
                   batch_size=128)
    W = np.asarray(W)

    intermediate_layer_model = Model(inputs=model.input,
                                 outputs=model.get_layer(layer_name).output)

    intermediate_output = intermediate_layer_model.predict(W)
    sa.saveAndDisplayResultKeras(intermediate_output[0],"sauvegardefichier.csv")
    return  intermediate_output[0]

NetworkCNN(600,2004,2019)