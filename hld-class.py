# classifying screenshots from the four different regions of the video game Hyper Light Drifter

from PIL import Image
import os

east = os.listdir(path='hldata/east')
eastimgs = []

for file in east:
	if file.endswith('.png'):
		im = Image.open("hldata/east/" + file)
		new = im.resize((30, 19))
		eastimgs.append(new)