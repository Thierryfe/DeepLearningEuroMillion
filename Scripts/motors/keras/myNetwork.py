import pandas as panda
import modules.parsing as parsing
import numpy as numpy
import os
import sys
import matplotlib.pyplot as plt
import tensorflow as tensorflow

from sklearn import model_selection
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN, Reshape, TimeDistributed, Embedding, GRU, Dropout
from tensorflow.keras.utils import plot_model
from tensorflow.keras.callbacks import ModelCheckpoint

def number_list():
    number_list = numpy.zeros((51,50))

    for i in range(1,number_list.shape[0]):
        number_list[i][i - 1] = 1

    return number_list

def data_form(year, to_year):
    data = parsing.setDataForTensorflow(year,to_year)

    data = numpy.insert(data, 0, 0, axis=1)

    data = numpy.insert(data, data.shape[1], 0, axis=1)

    list_nb = number_list()

    data_transform = []

    for i in range(data.shape[0]):
        tmp = []
        for j in range(data.shape[1]):
            number = data.item((i,j))
            tmp.append(list_nb[number])
        data_transform.append(tmp)

    data_final = numpy.array(data_transform)

    input_data = data_final[:,:-1]

    output_data = data_final[:,1:]

    input_train, input_test, output_train, output_test = model_selection.train_test_split(input_data, output_data, test_size = int(data.shape[0] * 0.3), random_state = 1)

    return input_train, input_test, output_train, output_test

def network(units = 50, epochs = 100, batch_size = 32):
    input_train, input_test, output_train, output_test = data_form(2004, 2020)

    model = Sequential()

    model.add(GRU(units = units, input_shape = (8,50), return_sequences = True, activation="tanh"))

    model.add(Dropout(0.2))

    model.add(GRU(units = units, return_sequences = True, activation = "tanh"))

    model.add(Dropout(0.2))

    model.add(TimeDistributed(Dense(units = 50, activation = "softmax")))

    mcp_save = ModelCheckpoint("keras_model_weights.h5", save_best_only=True, monitor='loss', mode='min', verbose=0)

    model.compile(loss = "categorical_crossentropy", optimizer = "adam", metrics = ["accuracy"])

    plot_path = os.path.join(os.path.realpath("."), "plot")
    plot_name = "model_" + str(units) + "_" + str(epochs) + "_" + str(batch_size)

    plot_model(model, to_file = plot_path + plot_name, show_shapes=True, show_layer_names=True, rankdir='TB')

    log = model.fit(input_train, output_train, epochs = epochs, batch_size = batch_size, callbacks=[mcp_save])

    log_history = log.history["acc"]
    plt.figure()
    plt.plot(numpy.arange(len(log_history)), log_history, marker='o', color='b', label='accuracy')
    plt.xlabel("Epoch")
    plt.ylabel("accuracy history")
    plt.grid()
    plt.show()

def evaluate():
    numpy.set_printoptions(threshold=sys.maxsize)

    input_train, input_test, output_train, output_test = data()

    model = tensorflow.keras.models.load_model("keras_model_weights.h5")

    pred = model.predict(input_test)

    score = model.evaluate(pred, output_test)

    print(score)

def predict():
    numpy.set_printoptions(threshold=sys.maxsize)

    list_nb = number_list()

    start = numpy.zeros((8,50))
    
    start = numpy.expand_dims(start, axis=0)

    model = tensorflow.keras.models.load_model("keras_model_weights.h5")

    tirage = []

    for i in range(8):
        pred = model.predict(start, steps = 8)

        number = numpy.argmax(pred[0][i]) + 1

        tirage.append(number)

        tmp = list_nb[number]

        start = numpy.insert(start[0], i + 1, tmp, axis = 0)

        start = start[:-1,:]

        start = numpy.expand_dims(start, axis=0)

    print(tirage)