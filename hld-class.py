# classifying screenshots from the four different regions of the video game Hyper Light Drifter

from PIL import Image
import os

east = os.listdir(path='hldata/east')
north = os.listdir(path='hldata/north')
west = os.listdir(path='hldata/west')
south = os.listdir(path='hldata/south')

def resizeimg(region, regionname):
	imlist = []
	for file in region:
		if file.endswith('.png'):
			im = Image.open("hldata/" + regionname + "/" + file)
			new = im.resize((30, 19))
			imlist.append(new)
	return imlist

eastimgs = resizeimg(east, "east")
northimgs = resizeimg(north, "north")
westimgs = resizeimg(west, "west")
southimgs = resizeimg(south, "south")

def saveimg(imlist, regionname):
	count = 1
	for img in imlist:
		img.save("data/" + regionname + "/" + count, "JPEG")
		count = count + 1

saveimg(east, "east")
saveimg(north, "north")
saveimg(west, "west")
saveimg(south, "south")