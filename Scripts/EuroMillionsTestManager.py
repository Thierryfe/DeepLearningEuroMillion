# coding=utf-8
'''
Auteur description : Thierry Fernandez
Date modification : 14/10/20
Description :
Script ayant pour objectif de contenir tout le programme de tests des divers moteurs en faisant appel à tous les modules developpés.

Developpeur :
'''


import numpy as np
from Scripts.Modules import Parsing
from Scripts.Motors.TensorFlow import Networks as euroMilNet
from Scripts.Modules import Logger

#import data
data = Parsing.setDataForTensorflow()


#prepare data from the numpy vector returned by the parser to two separated arrays of numbers and stars
numbers, stars = euroMilNet.prepare_data(data)
numbers_labels = numbers[1:len(numbers)-1]

#parameters of the network and learning
numbers_nb_inputs = 5
numbers_nb_outputs = 5
stars_nb_inputs = 5
stars_nb_outputs = 2
learning_rate = 0.001
nb_iterations = 50000
nb_RNeurons = 128



#Predict a number
predicted_number,numsLog = euroMilNet.euroMillionRnn(data=data, datainput=numbers,dataoutput= numbers_labels,
                                             number_inputs= numbers_nb_inputs, number_outputs= numbers_nb_outputs,
                                             learnin_Rate=learning_rate, number_of_iterations=nb_iterations, number_of_neurons=nb_RNeurons,
                                             model_name= "Numbers")

#prepare input for stars with adding the predicted number to the end of the numbers array
stars_input=[]
for number in numbers:
    stars_input.append(number)

stars_input.append(predicted_number)
stars_input= np.array(stars_input)

#predict stars from numbers
predicted_stars,starsLog = euroMilNet.euroMillionRnn(data=data, datainput=stars_input,dataoutput= stars,
                                             number_inputs= stars_nb_inputs, number_outputs= stars_nb_outputs,
                                             learnin_Rate=learning_rate, number_of_iterations=nb_iterations, number_of_neurons=nb_RNeurons,
                                             model_name= "Stars")
#logging
numsLog+=starsLog + "\nTHE FULL PREDICTION ! : \n" + str(predicted_number) + str(predicted_stars)
Logger.writeLog("euroMilNet.euroMillionRnn()","INFO", numsLog)


#the predicted full combination
print(str(predicted_number) + str(predicted_stars))

