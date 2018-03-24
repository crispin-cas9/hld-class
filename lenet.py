# https://www.pyimagesearch.com/2017/12/11/image-classification-with-keras-and-deep-learning/

# import the necessary packages
from keras.models import Sequential
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation
from keras.layers.core import Flatten
from keras.layers.core import Dense
from keras import backend as K


def lenetbuild(width, height, depth, classes):
	# initialize the model
	model = Sequential()
	inputShape = (height, width, depth)

	# if we are using "channels first", update the input shape
	if K.image_data_format() == "channels_first":
		inputShape = (depth, height, width)
	
	# another conv layer
	# model.add(Conv2D(20, (5, 5), padding="same", input_shape=inputShape))
# 	model.add(Activation("relu"))
	
	# first set of CONV => RELU => POOL layers
	model.add(Conv2D(20, (5, 5), padding="same", input_shape=inputShape))
	model.add(Activation("relu"))
	model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
	
	# second set of CONV => RELU => POOL layers
	model.add(Conv2D(50, (5, 5), padding="same"))
	model.add(Activation("relu"))
	model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
	
	# another conv layer
	model.add(Conv2D(20, (5, 5), padding="same", input_shape=inputShape))
	model.add(Activation("relu"))
	
	# first (and only) set of FC => RELU layers
	model.add(Flatten())
	model.add(Dense(500))
	model.add(Activation("relu"))

	# softmax classifier
	model.add(Dense(classes))
	model.add(Activation("softmax"))

	# return the constructed network architecture
	return model



