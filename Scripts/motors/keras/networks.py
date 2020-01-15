'''
Auteur description : Thierry Fernandez
Date modification : 14/10/20
Description :
Script contenant les différentes implémentations de réseaux de neurones à l'aide de Keras
Developpeur :
'''

from __future__ import print_function
import tensorflow as tf
from tensorflow.keras import Model
from tensorflow import keras
from tensorflow.keras import backend as K
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten,SimpleRNN

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

import modules.displayer as d
import modules.parsing as p
import modules.updater as u

"""
import Scripts.Modules.Displayer as d
import Scripts.Modules.Parsing as p
import Scripts.Modules.Updater as u
"""


#=======================================================================================================================
#=======================================================================================================================

import numpy as np
# ----------------------------------------------------------------------------------------
# ------------------------- CREATION FONCTION NETWORK CNN---------------------------------
# ----------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------

def NetworkCNN(Nb_Epoch,date1,date2):

# ----------------------------------------------------------------------------------------

# ---------------------------------------------
# ---------- PREPARATION DONNEE ---------------
# ---------------------------------------------

# ---------------------------------------------
#récupetration des données du jeu d'entrainement
# ---------------------------------------------
    Y=p.SetDataForKeras(date1, date2)
    tabresultat =p.KerasSetResultat(Y)

# ---------------------------------------------
# Définition d'un tagname pour la lastlayer
# ---------------------------------------------

    layer_name = "numero"

# ---------------------------------------------
#récuperation de la dernière valeur des datas, avec laquel on demandera un predict
# ---------------------------------------------

    W = [Y[-1]]
    W = np.asarray(W)

# ---------------------------------------------
#jeu d'entrainement auqeul on enleve le dernier
# ---------------------------------------------

    M = np.delete(Y, (-1), axis=0)

# ---------------------------------------------
#----------- DEFINITION DU RESEAU -------------
# ---------------------------------------------

# ---------------------------------------------
#On crée le model, on initialise un reseau de neurone vide
# ---------------------------------------------

    model = Sequential()

# ---------------------------------------------
#Ajout couche entré en precisant
# la dimension des données en entrée un tableau de taille 7
#Avec comme fonction d'activation une relu
# ---------------------------------------------

    model.add(Dense(89, input_dim=7, activation='relu'))

# ---------------------------------------------
#On ajoute de Dropout, qui sont la pour arreter certains neurones aléatoirement
# permt d'éviter le surapprenstissage n desactivant des neurones à chaque epoch
# ---------------------------------------------

    model.add(Dropout(0.5))

# ---------------------------------------------
#Ajout couche caché (hidden layer) de taille 78
# avec comme fonction d'acivation une relu
# ---------------------------------------------

    model.add(Dense(78, activation='relu'))

# ---------------------------------------------
#On ajoute de Dropout, qui sont la pour arreter certains neurones aléatoirement
# permt d'éviter le surapprenstissage n desactivant des neurones à chaque epoch
# ---------------------------------------------

    model.add(Dropout(0.5))

# ---------------------------------------------
# Création d'une couche separement
# on dit qu'elle renvoie un tableau de taille 62
# avec le tagname qui lui est attribué
# avec comme fonction d'acivation une sigmoid
# ---------------------------------------------

    last = Dense(62, activation='sigmoid',name=layer_name)

# ---------------------------------------------
#Ajout de la couche définis précédemennt
# ---------------------------------------------

    model.add(last)

# ---------------------------------------------
# On définit maintenant quelle sera la fonction de perte pour le model,
# et l'optimizer pour la vitesse, pas très important dans notre cas
# ---------------------------------------------

    model.compile(loss='binary_crossentropy',
              optimizer='rmsprop', )

# ---------------------------------------------
#On passe à l'entrainement, on donne en premier le jeu d'entrainement d'entrée, et celui de sortis
# pour pouvoir corriger ces erreurs, on lui indiqie le nombre d'epoch correspondant au nombres
# de fois ou il va faire les test, et le nombre de batch le nombre de fois ou il parcours le reseau avant
# de faire les calculs de correction, permet d'éviter d'avoir trop de calcul
# On peut le faire à 128 mais pour 600 epoch on est à 4mn d'attente
# ---------------------------------------------

    model.fit(M, tabresultat,
                   epochs=Nb_Epoch,
                   batch_size=128)

# ---------------------------------------------
# --------- RECUPERATION RESULTAT -------------
# ---------------------------------------------

# ---------------------------------------------
#permet de recuperer la dernière sortis du model
# le input sers à choisir qu'elle model on va " ecouter"
#et le output permet de recupérer la ligne avant le tagname correspondant
# ---------------------------------------------

    intermediate_layer_model = Model(inputs=model.input,
                                 outputs=model.get_layer(layer_name).output)
# ---------------------------------------------
#on demande au reseau de neurone de nous fournir une réponse pour la donnée en entrée
# on utilise la utilise la ligne audessus qui reprend le model precedent, mais lors de la prediction nous renvoie
# en plus le tableau de valeur correspondant
# W est le tirage le plus recent, car normalement les tableau se mettent à jour
# ---------------------------------------------

    intermediate_output = intermediate_layer_model.predict(W)

# ---------------------------------------------
#apelle de la fonction pour que la mise en forme de nos chiffres
# ---------------------------------------------

    d.saveAndDisplayResultKeras(intermediate_output[0],"sauvegardefichier.csv")

# ---------------------------------------------
# permet de récupérer le tirage apres appelle de la fonction
# ---------------------------------------------
    print(W)
    return  intermediate_output[0]

# ---------------------------------------------
# ---------------------------------------------
# ----------------------------------------------------------------------------------------
#finfonction

# ---------------------------------------------
# Exemple utilisation fonction , on fixe le nombre d'epo, les dates entre les tirages
# ---------------------------------------------

#NetworkCNN(6000,2004,2019)

#=======================================================================================================================
#=======================================================================================================================

# ----------------------------------------------------------------------------------------
# ------------------------- CREATION FONCTION NETWORK RNN---------------------------------
# ----------------------------------------------------------------------------------------

def NetworkRNN(Nb_epoch,date1,date2):

# ----------------------------------------------------------------------------------------

# ---------------------------------------------
# ---------- PREPARATION DONNEE ---------------
# ---------------------------------------------

# ---------------------------------------------
#récupetration des données du jeu d'entrainement
# ---------------------------------------------

    Y=p.SetDataForKeras(date1,date2)
    tabresultat=p.KerasSetResultat(Y)

# ---------------------------------------------
# Définition d'un tagname pour la lastlayer
# ---------------------------------------------
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
    M = np.reshape(M, (M.shape[0], 1, M.shape[1]))
   # M1 = np.reshape(M1, (M1.shape[0], 1, M1.shape[1]))

# ---------------------------------------------
#----------- DEFINITION DU RESEAU -------------
# ---------------------------------------------

# ---------------------------------------------
#On crée le model, on initialise un reseau de neurone vide
# ---------------------------------------------

    model = Sequential()

# ---------------------------------------------
#Ajout couche entré en precisant le fait qu'il soit Rnn
#on regle les unités oour eviter des problémes de typages
#On donne la dimension des données en entrée un tableau de taille 7
#Avec comme fonction d'activation une relu
# ---------------------------------------------

    model.add(SimpleRNN(units=32, input_shape=(1,7), activation="relu"))

# ---------------------------------------------
#Ajout d"une couche de neurone (layer) de taille 64 avec fonction d'activation une relu
# ---------------------------------------------

    model.add(Dense(64, activation="relu"))

# ---------------------------------------------
#Création couche de taille 7, avec un nom pour pouvoir récupérer les résulats après.
# ---------------------------------------------

    last=Dense(7,name=lastname)

# ---------------------------------------------
#On ajoute la couche au reseau
# ---------------------------------------------

    model.add(last)

# ---------------------------------------------
# On définit maintenant quelle sera la fonction de perte pour le model,
# et l'optimizer pour la vitesse, pas très important dans notre cas
# ---------------------------------------------

    model.compile(loss='mean_squared_error', optimizer='rmsprop')

# ---------------------------------------------
#On passe à l'entrainement, on donne en premier le jeu d'entrainement d'entrée, et celui de sortis
# pour pouvoir corriger ces erreurs, on lui indiqie le nombre d'epoch correspondant au nombres
# de fois ou il va faire les test, et le nombre de batch le nombre de fois ou il parcours le reseau avant
# de faire les calculs de correction, permet d'éviter d'avoir trop de calcul
# On peut le faire à 1 mais pour 100 epoch on est à 10mn d'attente
# une bonne taille est 16 permettant pour 100, d'avoir un temps d'attente correct
# ---------------------------------------------

    model.fit(M,M1, epochs=Nb_epoch, batch_size=16, verbose=2)

# ---------------------------------------------
# --------- RECUPERATION RESULTAT -------------
# ---------------------------------------------

# ---------------------------------------------
#permet de recuperer la dernière sortis du model
# le input sers à choisir qu'elle model on va " ecouter"
#et le output permet de recupérer la ligne avant le tagname correspondant
# ---------------------------------------------

    intermediate_layer_model = Model(inputs=model.input,
                                 outputs=model.get_layer(lastname).output)

# ---------------------------------------------
#on demande au reseau de neurone de nous fournir une réponse pour la donnée en entrée
# on utilise la utilise la ligne audessus qui reprend le model precedent, mais lors de la prediction nous renvoie
# en plus le tableau de valeur correspondant
# W est le tirage le plus recent, car normalement les tableau se mettent à jour
# ---------------------------------------------

    intermediate_output = intermediate_layer_model.predict(W)

# ---------------------------------------------
#apelle de la fonction pour que la mise en forme de nos chiffres
# ---------------------------------------------

    d.saveAndDisplayResultKerasRnn(intermediate_output[0],"sauvegardefichierRNN.csv")

# ---------------------------------------------
# permet de récupérer le tirage apres appelle de la fonction
# ---------------------------------------------

    return intermediate_output[0]

# ---------------------------------------------
# ---------------------------------------------
# ----------------------------------------------------------------------------------------
#finfonction

# ---------------------------------------------
# Exemple utilisation fonction , on fixe le nombre d'epo, les dates entre les tirages
# ---------------------------------------------

#NetworkRNN(6000,2004,2019)

# ---------------------------------------------



