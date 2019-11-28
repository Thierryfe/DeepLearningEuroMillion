from __future__ import print_function
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import backend as K
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten,SimpleRNN

import SetDataForKeras
from SetDataForKeras import csvtotabforkeras
import numpy as np
from KerasSetResultat import KerasSetResultat
import pandas as pnd


Y=csvtotabforkeras(2004,2019);

tabresultat=KerasSetResultat(Y)


M=np.delete(Y, (-1), axis=0)


#trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
#testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

#print("vauuuux",trainX[1])

model = Sequential()
model.add(SimpleRNN(units=32, input_dim=7, activation="relu"))
output=model.add(Dense(64, activation="relu"))
model.add(Dense(7))
model.compile(loss='mean_squared_error', optimizer='rmsprop')
model.summary()

model.fit(M,M, epochs=100, batch_size=16, verbose=2)
#trainPredict = model.predict(trainX)

#print("alors ",trainPredict)
#testPredict= model.predict(testX)
#predicted=np.concatenate((trainPredict,testPredict),axis=0)

#trainScore = model.evaluate(trainX, trainY, verbose=0)