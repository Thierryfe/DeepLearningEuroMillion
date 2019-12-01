from __future__ import print_function
import tensorflow as tf
from tensorflow.keras import Model
from tensorflow import keras
from tensorflow.keras import backend as K
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten,SimpleRNN

import Scripts.Modules.KerasSetResultat as sr
import Scripts.Modules.saveAndDisplayResultKerasRnn as sa
import Scripts.Modules.SetDataForKeras as sd
import numpy as np

def NetworkRNN(Nb_epoch,date1,date2):
# ---------------------------------------------
#récupetration des données du jeu d'entrainement
# ---------------------------------------------

    Y=sd.SetDataForKeras(date1,date2);
    tabresultat=sr.KerasSetResultat(Y)
    lastname="dernierecouche"

# ---------------------------------------------
#récuperation de la dernière valeur des datas, avec laquel on demandera un predict
# ---------------------------------------------

    W=np.asarray([[Y[-1]]])

# ---------------------------------------------
#jeu d'entrainement auqeul on enleve le dernier
# ---------------------------------------------

    M=np.delete(Y, (-1), axis=0)

# ---------------------------------------------
#jeu de correction lors de l'entrainement auquel on enleve le premier
# ---------------------------------------------

    M1=np.delete(Y, (0), axis=0)

# ---------------------------------------------
#mise en forme pour la lecture par le reseaux de neurones
# ---------------------------------------------

    M1 = np.reshape(M1, (M1.shape[0], 1, M1.shape[1]))

# ---------------------------------------------
#Notre reseau de neurones, ici en rnn
# ---------------------------------------------

    model = Sequential()
    model.add(SimpleRNN(units=32, input_shape=(1,7), activation="relu"))
    model.add(Dense(64, activation="relu"))
    last=Dense(7,name=lastname)
    model.add(last)
    model.compile(loss='mean_squared_error', optimizer='rmsprop')
    model.fit(M1,M, epochs=Nb_epoch, batch_size=16, verbose=2)

# ---------------------------------------------
#permet de recuperer la dernière sortis du model
# ---------------------------------------------

    intermediate_layer_model = Model(inputs=model.input,
                                 outputs=model.get_layer(lastname).output)

# ---------------------------------------------
#ici oon demande au reseau de neurone de nous fournir une réponse pour la donnée en entrée
# ---------------------------------------------

    intermediate_output = intermediate_layer_model.predict(W)

# ---------------------------------------------
#apelle de la fonction pour que la mise en forme de nos chiffres
# ---------------------------------------------

    sa.saveAndDisplayResultKerasRnn(intermediate_output[0],"sauvegardefichierRNN.csv")
    return intermediate_output[0]

NetworkRNN(100,2004,2019)