from motors.keras.myNetwork import *

for i in range(2,8,2):
	network(units = 32, epochs = 64*i, batch_size = 32)

for i in range(2,8,2):
	network(units = 64, epochs = 64*i, batch_size = 32)

for i in range(2,8,2):
	network(units = 128, epochs = 64*i, batch_size = 32)

for i in range(2,8,2):
	network(units = 32, epochs = 64*i, batch_size = 64)

for i in range(2,8,2):
	network(units = 64, epochs = 64*i, batch_size = 64)

for i in range(2,8,2):
	network(units = 128, epochs = 64*i, batch_size = 64)

evaluate()
predict()