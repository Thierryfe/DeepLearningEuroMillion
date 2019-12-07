# coding=utf-8
'''
Auteur description : Thierry Fernandez
Date modification : 14/10/20
Description :
Script ayant pour objectif de contenir tout le programme de tests des divers moteurs en faisant appel à tous les modules developpés.

Developpeur :
'''

import Modules.Updater as ud
import Modules.Parsing as pa
import Modules.Displayer as di
import Modules.Logger as lo

import Motors.Keras.Networks as net

#ud.update()

net.NetworkCNN(60000,2004,2019)
net.NetworkRNN(60000,2004,2019)