# classifying screenshots from the four different regions of the video game Hyper Light Drifter

from PIL import Image
import os

east = os.listdir(path='hldata/east')
north = os.listdir(path='hldata/north')
west = os.listdir(path='hldata/west')
south = os.listdir(path='hldata/south')

def resizeimg(region, regionname):
	for file in region:
		if file.endswith('.jpg'):
			name = "hldata/" + regionname + "/" + file
			im = Image.open(name)
			new = im.resize((30, 19))
			new = new.convert("RGB")
			new.save(name)

# resizeimg(east, "east")
# resizeimg(north, "north")
# resizeimg(west, "west")
# resizeimg(south, "south")

def renameimg(region, regionname):
	count = 1
	for file in region:
		if file.endswith('.png'):
			os.rename("hldata/" + regionname + "/" + file, "hldata/" + regionname + "/" + str(count) + '.jpg')
			count = count + 1

renameimg(east, "east")
renameimg(north, "north")
renameimg(west, "west")
renameimg(south, "south")