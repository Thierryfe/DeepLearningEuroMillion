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

#import Modules.Updater as ud
#import Modules.Parsing as pa
#import Modules.Displayer as di
#import Modules.Logger as lo

#import Motors.Keras.Networks as net
"""
ud.update()
#import data
annee_actuelle = datetime.datetime.now().year
data = Parsing.setDataForTensorflow(2004,annee_actuelle)
print(len(data))


#séparation des numéros et numéros étoiles
numbers, stars = euroMilNet.prepare_data(data)

#création des labels pour les numéros (pour chaque tirage en entrée, son label et le tirage qui le suit )
numbers_labels = numbers[1:len(numbers)-1]

#parametres du Modele
numbers_nb_inputs = 5  #numéro des entrées ( pour les numéros )
numbers_nb_outputs = 5 #numéro des sorties ( pour les numéros )
stars_nb_inputs = 5 #numéro des entrées ( pour les numéros etoiles )
stars_nb_outputs = 2 #numéro des sorties ( pour les numéros etoiles )

#parametres d'aaprentissage
learning_rate = 0.001
nb_iterations = 200
nb_RNeurons = 128


# prédiction des prochains 5 numéros
predicted_number,numsLog = euroMilNet.euroMillionRnn(data=data, datainput=numbers,dataoutput= numbers_labels,
                                             number_inputs= numbers_nb_inputs, number_outputs= numbers_nb_outputs,
                                             learnin_Rate=learning_rate, number_of_iterations=nb_iterations, number_of_neurons=nb_RNeurons,
                                             model_name= "Numbers")



#ajout du nombre prédit dans le tableau des entrés des etoiles pour lui prédire les numéros étoiles
stars_input=[]
for number in numbers:
    stars_input.append(number)

stars_input.append(predicted_number)
stars_input= np.array(stars_input)

#prediction des numeros etoiles à partir du numéro déja prédit
predicted_stars,starsLog = euroMilNet.euroMillionRnn(data=data, datainput=stars_input,dataoutput= stars,
                                             number_inputs= stars_nb_inputs, number_outputs= stars_nb_outputs,
                                             learnin_Rate=learning_rate, number_of_iterations=nb_iterations, number_of_neurons=nb_RNeurons,
                                             model_name= "Stars")
#logging
numsLog+=starsLog + "\nTHE FULL PREDICTION ! : \n" + str(predicted_number) + str(predicted_stars)
Logger.writeLog("euroMilNet.euroMillionRnn()","INFO", numsLog)


#the predicted full combination
print(str(predicted_number) + str(predicted_stars))
"""
#net.NetworkCNN(60000,2004,2019)
#net.NetworkRNN(60000,2004,2019)

writeLog('test', 'WARNING', 'coucou')
