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
from motors.keras.myNetwork import *
from motors.tensorFlow.networks import *

nbTirages=0
nbNeurones=0
#Si il n'y a pas d'argument, on passe en mode manuel
if(len(sys.argv)==1):
	download = input('Voulez vous télécharger (ou mettre à jour) les données de l\'Euromillion (y/n) ?')
	framework = input('Voulez vous utiliser tensorflow ou keras ?\n')
	if(framework=='tensorflow'):
		print("tensorflow")
		reseau='RNN'
	elif(framework=='keras'):
		reseau = input('Quel réseau de neurones voulez vous entrainer ? RNN ou CNN ou RNN2 (meilleure version de RNN)\n')
	if(reseau=='RNN2'):
		nbNeurones = input('Combien de neurones voulez vous sur les couches 2 et 3 ?')
		nbTirages = input('Combien de tirages voulez vous utiliser en même temps ? (batch size)')
	nbIter = input('Combien voulez-vous d\'itérations ?\n')
	dateDebut = input('Veuillez choisir l\'intervalle (date entre 2004 et l\'année courante) sur lequel vous voulez traviller\nDate de début ? ')
	dateFin = input('Date de fin ? ')
elif(len(sys.argv)==9):
	download=sys.argv[1]
	framework=sys.argv[2]
	reseau=sys.argv[3]
	nbNeurones=sys.argv[4]
	nbTirages=sys.argv[5]
	nbIter=sys.argv[6]
	dateDebut=sys.argv[7]
	dateFin=sys.argv[8]
else:
	print('Il n\'y a pas assez d\'arguments\nVeuillez relancer le script\n')
	sys.exit()

#On cast les chaines de caractères en int pour qu'elles puissent être utilisées par nos applications
nbTirages=int(nbTirages)
nbNeurones=int(nbNeurones)
nbIter=int(nbIter)
dateDebut=int(dateDebut)
dateFin=int(dateFin)

if(download=='y'):
	update()
elif(download=='n'):
	print('Les données ne vont pas être téléchargées (ou mise à jour)')
else:
	print('Les arguments sont incorrects')
	sys.exit()
if(framework=='keras'):
	if(reseau=='RNN'):
		NetworkRNN(nbIter,dateDebut,dateFin)
	elif(reseau=='CNN'):
		NetworkCNN(nbIter,dateDebut,dateFin)
	elif(reseau=='RNN2'):
		network(nbNeurones,nbIter,nbTirages,dateDebut,dateFin)
		evaluate(dateDebut,dateFin)
		predict()
elif(framework=='tensorflow'):
	if(reseau=='RNN'):
		launch(nbTirages,dateDebut,dateFin)
	elif(reseau=='CNN'):
		print('Il n\'est pas possible de possible de faire du CNN avec notre moteur tensorflow (préférez keras pour du CNN)')
else:
	print('Les arguments sont incorrects')
	sys.exit()


#pour exécuter les script avec les paramètre download=yes framework=keras reseau=RNN nombre d'iteration = 100 date_debut=2004 et date_fin=2020
#python EuroMillionsTestManager.py y keras RNN 100 2004 2020


	

