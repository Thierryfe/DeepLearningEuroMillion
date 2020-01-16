# coding=utf-8
'''
Auteur description : Thierry Fernandez
Date modification : 14/10/20
Description :
Script ayant pour objectif de contenir tout le programme de tests des divers moteurs en faisant appel à tous les modules developpés.

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
		reseau='RNN'
	elif(moteur=='keras'):
		reseau = input('Quel réseau de neurones voulez vous entrainer ? RNN ou CNN\n')
	nbIter = input('Combien voulez-vous d\'itérations ?\n')
	dateDebut = input('Veuillez choisir l\'intervalle (date entre 2004 et l\'année courante) sur lequel vous voulez traviller\nDate de début ? ')
	dateFin = input('Date de fin ? ')
elif(len(sys.argv)==7):
	reponse=sys.argv[1]
	moteur=sys.argv[2]
	reseau=sys.argv[3]
	nbIter=sys.argv[4]
	dateDebut=sys.argv[5]
	dateFin=sys.argv[6]
else:
	print('Il n\'y a pas assez d\'arguments\nVeuillez relancer le script\n')
	sys.exit()

nbIter=int(nbIter)
dateDebut=int(dateDebut)
dateFin=int(dateFin)

if(reponse=='y'):
	update()
elif(reponse=='n'):
	print('Les données ne vont pas être téléchargées (ou mise à jour)')
else:
	print('Les arguments sont incorrects')
	sys.exit()
if(moteur=='keras'):
	if(reseau=='RNN'):
		NetworkRNN(nbIter,dateDebut,dateFin)
	elif(reseau=='CNN'):
		NetworkCNN(nbIter,dateDebut,dateFin)
elif(moteur=='tensorflow'):
	if(reseau=='RNN'):
		launch()
	elif(reseau=='CNN'):
		print('Il n\'est pas possible de possible de faire du CNN avec notre moteur tensorflow (préférez keras pour du CNN)')
else:
	print('Les arguments sont incorrects')
	sys.exit()


#pour exécuter les script avec les paramètre update=yes moteur=keras reseau=RNN nombre d'iteration = 100 date_debut=2004 et date_fin=2020
#python EuroMillionsTestManager.py y keras RNN 100 2004 2020


	

