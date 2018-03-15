# classifying screenshots from the four different regions of the video game Hyper Light Drifter

# don't run this; it's not needed for classification

from PIL import Image
import os
import numpy

east = os.listdir(path='hldata/east')
north = os.listdir(path='hldata/north')
west = os.listdir(path='hldata/west')
south = os.listdir(path='hldata/south')

def toarray(region, regionname):
	imlist = []
	for file in region:
		if file.endswith('.jpg'):
			im = Image.open("hldata/" + regionname + "/" + file)
			imlist.append(numpy.array(im))
	return imlist

eastlist = toarray(east, "east")
northlist = toarray(north, "north")
westlist = toarray(west, "west")
southlist = toarray(south, "south")