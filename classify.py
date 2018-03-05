# classifying screenshots from the four different regions of the video game Hyper Light Drifter

from PIL import Image
import os

east = os.listdir(path='hldata/east')
north = os.listdir(path='hldata/north')
west = os.listdir(path='hldata/west')
south = os.listdir(path='hldata/south')

def imgbytes(region, regionname):
	imlist = []
	for file in region:
		if file.endswith('.png'):
			im = Image.open("hldata/" + regionname + "/" + file)
			imlist.append(im.tobytes())
	return imlist

testlist = imgbytes(east, "east")

print(testlist[0])