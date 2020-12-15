# Adatped from Jason Brownlee
# Author: Urjeet Deshmukh, December 12th, 2020

from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense

# Load the data set
dataset = loadtxt('pima-natives-diabetes.csv', delimiter = ',')
# Split into input (x) and output (y) variables
x = dataset[:, 0:8]		# Copy full row and columns 0-7
y = dataset[:, 8]		# Copy full row and column 8

# Define the Keras model
model = Sequential()
model.add(Dense(12, input_dim = 8, activation = 'relu'))
model.add(Dense(8, activation = 'relu'))
model.add(Dense(1, activation = 'sigmoid'))

# Compile the Keras model
model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

# Fit the Keras model on the dataset
model.fit(x, y, epochs = 150, batch_size = 10)

# Evaluate the Keras model
_, accuracy = model.evaluate(x, y)
print('\nAccuracy: %.2f' % (accuracy * 100), '\n')

# Make class predictions with the model
predictions = model.predict_classes(x)

# Summarize the first 5 cases
print('\n')
for i in range(5):
	print('%s => Predicted: %d; Expected: %d' % (x[i].tolist(), predictions[i], y[i]))