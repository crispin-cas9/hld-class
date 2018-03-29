# https://www.pyimagesearch.com/2017/12/11/image-classification-with-keras-and-deep-learning/

# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2
import os


# argument parse - add command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path to trained model model")
# ap.add_argument("-i", "--image", required=True,
# 	help="path to input image")
args = vars(ap.parse_args())

def testimg(img, count):

	# load the image and copy it
	#image = cv2.imread(args["image"])
	image = cv2.imread(img)
	orig = image.copy()
 
	# pre-process the image for classification
	image = cv2.resize(image, (28, 28))
	image = image.astype("float") / 255.0
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)

	# load the trained convolutional neural network
	print("[INFO] loading network...")
	model = load_model(args["model"])
 
	# classify the input image
	(east, north, west, south) = model.predict(image)[0]

	# build the labels (come back and make this more elegant later)
	if east > north and east > west and east > south:
		label = "East"
	if north > east and north > west and north > south:
		label = "North"
	if west > north and west > east and west > south:
		label = "West"
	if south > north and south > west and south > east:
		label = "South"

	eastlabel = "East " + str(round(east*100, 3))
	northlabel = "North: " + str(round(north*100, 3))
	westlabel = "West: " + str(round(west*100, 3))
	southlabel = "South: " + str(round(south*100, 3))
	
	#"{}: {:.2f}%".format(label, proba * 100)
 
	# draw the label on the image
	output = imutils.resize(orig, width=400)
	cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
		0.7, (255, 255, 255), 2)
	cv2.putText(output, eastlabel, (10, 50),  cv2.FONT_HERSHEY_SIMPLEX,
		0.6, (255, 255, 255), 2)
	cv2.putText(output, northlabel, (10, 75),  cv2.FONT_HERSHEY_SIMPLEX,
		0.6, (255, 255, 255), 2)
	cv2.putText(output, westlabel, (10, 100),  cv2.FONT_HERSHEY_SIMPLEX,
		0.6, (255, 255, 255), 2)
	cv2.putText(output, southlabel, (10, 125),  cv2.FONT_HERSHEY_SIMPLEX,
		0.6, (255, 255, 255), 2)
	
	cv2.imwrite("guesses/" + str(count) + "-test.jpg", output)
	
	# show the output image
	#cv2.imshow("Output", output)
	
testdata = os.listdir(path='testing')
count = 1

for file in testdata:
	if file.endswith('.jpg') or file.endswith('.png'):
		name = "testing/" + file
		testimg(name, count)
		count = count + 1


