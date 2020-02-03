# coding=utf-8
'''
Auteur description : Thierry Fernandez
Date modification : 14/10/20
Description : Script ayant pour objectif de contenir tout le programme de tests des divers moteurs en faisant appel à tous les modules developpés.

Developpeur :
'''

from modules.logger import *
from modules.displayer import *
from modules.updater import *
from motors.keras.networks import *
from motors.tensorFlow.networks import *

#Si il n'y a pas d'argument, on passe en mode manuel
if(len(sys.argv)==1):
	reponse = input('Voulez vous télécharger (ou mettre à jour) les données de l\'Euromillion (y/n) ')
	
	moteur = input('Voulez vous utiliser tensorflow ou keras ?\n')
	if(moteur=='tensorflow'):
		print("tensorflow")
	elif(moteur=='keras'):
		reseau = input('Quel réseau de neurones voulez vous entrainer ? RNN ou CNN\n')
elif(len(sys.argv)==7):
	reponse=sys.argv[1]
	moteur=sys.argv[2]
	reseau=sys.argv[3]
	nbIter=int(sys.argv[4])
	dateDebut=int(sys.argv[5])
	dateFin=int(sys.argv[6])
	print(dateDebut)
	print(dateFin)
else:
	print('Il n\'y a pas assez d\'arguments\nVeuillez relancer le script\n')


if(reponse=='y'):
		update()
if(moteur=='keras'):
	if(reseau=='RNN'):
		NetworkRNN(nbIter,dateDebut,dateFin)
	elif(reseau=='CNN'):
		NetworkCNN(nbIter,dateDebut,dateFin)

#pour exécuter les script avec les paramètre update=yes moteur=keras reseau=RNN nombre d'iteration = 100 date_debut=2004 et date_fin=2020
#python EuroMillionsTestManager.py y keras RNN 100 2004 2020


	

