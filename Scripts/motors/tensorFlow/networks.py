'''
Auteur description : Thierry Fernandez
Date modification : 14/10/20
Description :
Script contenant les différentes implémentations de réseaux de neurones à l'aide de TensorFlow
Developpeur :
'''


import tensorflow as tf
import numpy as np
import time
import datetime
from modules.logger import *
from modules.parsing import *
import pandas as panda



def test():
    data = parsing.setDataForTensorflow(2004,2019)
    dataPanda = panda.DataFrame(data)
    print(dataPanda.info())
start_time=time.time()

if __name__ == "__main__":
    test()


def launch(nb_iterations=200,dateDebut=2004,dateFin=2020):
    #import data
    data = setDataForTensorflow(dateDebut,dateFin)
    print(len(data))

    #séparation des numéros et numéros étoiles
    numbers, stars = prepare_data(data)

    #création des labels pour les numéros (pour chaque tirage en entrée, son label et le tirage qui le suit )
    numbers_labels = numbers[1:len(numbers)-1]

    #parametres du Modele
    numbers_nb_inputs = 5  #numéro des entrées ( pour les numéros )
    numbers_nb_outputs = 5 #numéro des sorties ( pour les numéros )
    stars_nb_inputs = 5 #numéro des entrées ( pour les numéros etoiles )
    stars_nb_outputs = 2 #numéro des sorties ( pour les numéros etoiles )

    #parametres d'aaprentissage
    learning_rate = 0.001
    nb_RNeurons = 128


    # prédiction des prochains 5 numéros
    predicted_number,numsLog = euroMillionRnn(data=data, datainput=numbers,dataoutput= numbers_labels,
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
    predicted_stars,starsLog = euroMillionRnn(data=data, datainput=stars_input,dataoutput= stars,
                                                 number_inputs= stars_nb_inputs, number_outputs= stars_nb_outputs,
                                                 learnin_Rate=learning_rate, number_of_iterations=nb_iterations, number_of_neurons=nb_RNeurons,
                                                 model_name= "Stars")
    #logging
    numsLog+=starsLog + "\nTHE FULL PREDICTION ! : \n" + str(predicted_number) + str(predicted_stars)
    writeLog("euroMilNet.euroMillionRnn()","INFO", numsLog)


    #the predicted full combination
    print(str(predicted_number) + str(predicted_stars))

#juste pour compter le temps pris par le RNN
def elapsed(start_time, finish_time):
    sec = finish_time - start_time
    if sec<60:
        return  "{:.2f} ".format(sec) + " seconds"
    else:
        return "{:.2f} ".format(sec//60) + " minutes and " +  "{:.2f} ".format(sec % 60) + " seconds"


#prepare draws for build_dataset
#prepare data returns two arrays 5*number_of_draws for the numbers of all th past draws and 2*number_of_draws for the stars of all th past draws.
def prepare_data(data):
    numbers = []
    stars = []
    for draw in data:
        number = []
        for i in range(0, 5):
            number.append(draw[0, i])
        numbers.append(number)
        star = []
        for i in range(5, 7):
            star.append(draw[0, i])
        stars.append(star)
    return np.array(numbers), np.array(stars)


'''#transfer data to one_hot format
def to_one_hot(draws,depth):
    draws_one_hot = []
    for draw in draws:
        draws_one_hot.append(tf.one_hot(draw, depth))
    return draws_one_hot
    # eg : [1,2,3,4,5] to [[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0], [0,0,0,1,0], [0,0,0,0,1]]'''


#Create a batch size between 2 and 21 to much our data size
def batch_size (vec):
    bs = 1
    for i in range(2, 21):
        if len(vec) % i == 0:
            bs = i
    return 10

def create_batches(train_data_input, train_data_output, input, output,size_train):
    ## Create X
        x_data = train_data_input[:size_train-1] # Select all the training instance minus one day
        X_batches = x_data.reshape(-1, 1, input)    # create the right shape for the batch e.g (10, batchsize, 5)
    ## Create y
        y_data = train_data_output[:size_train-1]
        y_batches = y_data.reshape(-1, 1, output)
        return X_batches, y_batches



#start the function here
def euroMillionRnn(data, datainput, dataoutput, number_inputs, number_outputs,learnin_Rate=0.001, number_of_iterations=100, number_of_neurons=128, model_name = "not named"):

    """créer le RNN,l'éxecuter, et retourne la prédiction et le log du modèle

        paramètres:
        data -- toutes les donées de tirages renveoyer par la fonction du parsing setDataForTensorflow()
        datainput -- les entrées (les cinqs numéros)
        dataoutput -- les labels qui seront comparés à la sortie avec les predictions du modele
        number_inputs -- le nombre des entrées ( 5 )
        number_outputs -- le nombre des sorties ( 5 pour les numéros et 2 pour les numeros etoiles
        learning rate -- le taux d'apprentissage
        number_of_iterations -- nombre d'iterations
        number_of_neurons -- nombre des neurones du modèle
        model_name -- le nom du model, utilisé da le log

        """

    logger = "\n\nloaded trainig data of " + str(len(data)) + " past draws... \n\nInitialization...\n\n"

    print("loaded trainig data of " + str(len(data)) + " past draws...\n Initialization...")

    #initialisation des parametres du modèle :

    n_input = number_inputs
    numbers_n_output = number_outputs

    size_train = int(len(data) * 4/5) #la taille des donées d'apprentissages, ici je choisis de prendre 4/5.

    ## Split data
    ###numbers
    train_numbers = datainput[:size_train]
    #test_numbers = datainput[size_train:]

    train_numbers_output = dataoutput[:size_train]
    #test_numbers_output = dataoutput[size_train:]

    n_windows = 2 #( combien de tirages par iteration)
                                             #le nombre des tirages n'est pas constant ( les mises à jours ) donc batch size()  est utiliser pour
                                             #fournir un batch (nombre de tirage en entrée par 1 iteration) entre 1 et 20 (le plus grand)


    #Creating X,Y batches for train and test
    X_batches, y_batches = create_batches(train_numbers,train_numbers_output,n_input,numbers_n_output,size_train)

    X_test, y_test = create_batches(train_numbers,train_numbers_output,n_input,numbers_n_output, size_train)


    tf.reset_default_graph()

    ##0.Parameteres d'apprentissage :
    learning_rate = learnin_Rate
    iterations = number_of_iterations
    r_neuron = number_of_neurons


    ## 1. création des tensors
    X = tf.placeholder(tf.float32, [None,n_windows-1,n_input])
    y_numbers = tf.placeholder(tf.float32, [None,n_windows-1,numbers_n_output])


    ## 2. creation du model
    basic_cell = tf.contrib.rnn.BasicRNNCell(num_units=r_neuron, activation=tf.nn.relu)
    numbers_rnn_output, numbers_states = tf.nn.dynamic_rnn(basic_cell, X, dtype=tf.float32)


    ## 3. Configuration du RNN
    numbers_stacked_rnn_output = tf.reshape(numbers_rnn_output, [-1, r_neuron])
    numbers_stacked_outputs = tf.layers.dense(numbers_stacked_rnn_output, numbers_n_output)
    numbers_outputs = tf.reshape(numbers_stacked_outputs, [-1,n_windows-1, numbers_n_output])

    ## perte et optimistation:
      #la perte = (prediction - labels)^2
    loss = tf.reduce_sum(tf.square(numbers_outputs - y_numbers))


      #Optimizer: reduire la perte: test sur deux optimasers possibles:
        #Opt1: with tf.train.AdamOptimizer(learning_rate=learning_rate) mse from 3M to 64K in 4500 iterations
    optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)

      #Opt2 with tf.train.RMSPropOptimizer(learning_rate=learning_rate) mse from 3M to 50K in 4500 iterations
       #optimizer = tf.train.RMSPropOptimizer(learning_rate=learning_rate)

    training_op = optimizer.minimize(loss)

    #initialisation des variables
    init = tf.global_variables_initializer()

    #l'evaluation du modele
    numbers_rnn_output.shape
    y_batches.shape
    correct_pred =tf.equal(tf.argmax(numbers_rnn_output,2), tf.argmax(y_batches, 2))
    accuaracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

    with tf.Session() as sess:
        sess.run(init)
        acc_total = 0
        loss_total = 0
        logger +="trainig started of the model: " + model_name+"\n"
        print("trainig started of the model: " + model_name)
        min_iteration,max_iteration = -1, -1
        min_mse =float("inf")
        max_acc = 0.0
        for iters in range(iterations):
            print(X)
            _, acc, los = sess.run([training_op, accuaracy, loss], feed_dict={X:X_batches, y_numbers:y_batches})
            if iters % 500 == 0:
                mse = loss.eval(feed_dict={X: X_batches, y_numbers: y_batches})
                loss_total += los
                acc_total += acc
                print(iters, "\tMSE:", mse, " Average Loss: " + "{:.6f} ".format(loss_total/iters) + " accuaracy: {:.50f}% ".format(100*acc_total/iters)+"max accuaracy:{:.50f}% ".format(max_acc)+ " in iteration: " + str(max_iteration) )
                if mse<min_mse :
                    min_mse = mse
                    min_iteration = iters
                if max_acc< 100*acc_total/iters:
                    max_acc = 100*acc_total/iters
                    max_iteration = iters

        now = time.time()
        print("\n\nTraining to predict " + model_name +" finished after :[" + str(iterations) + "] iterations in: ["+ elapsed(start_time, now) +
              "]\n With minimum MSE of: [" + str(min_mse) +"] at the iteration: [" +str(min_iteration) +
              "]\n And max accuaracy:[{:.50f}%] ".format(max_acc)+ " at iteration: [" + max_iteration.__str__()+"]")

        #test du modele et recuperation du tableau de tout les predictions, on prend juste le dernier
        y_pred = sess.run(numbers_outputs, feed_dict={X: X_test})
        next_number_prediction_floats = y_pred[len(y_pred)-1, n_windows-2]
        next_number_prediction_int = []
        for number in next_number_prediction_floats:
            next_number_prediction_int.append(int(number))

        logger += "\n\nTraining to predict " + model_name +" finished after :[" + str(iterations) + "] iterations in: [" + elapsed(start_time,  now) +\
                  "]\n With minimum MSE of: [" + str(min_mse) + "] at the iteration: [" + str(min_iteration) +"]\n And max accuaracy:[{:.50f}%] ".format(  max_acc) +\
                  " at iteration: [" + max_iteration.__str__() + "] and predicted " + str(next_number_prediction_int)

        return next_number_prediction_int,logger
