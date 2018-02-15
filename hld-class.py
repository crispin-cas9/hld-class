# classifying screenshots from the four different regions of the video game Hyper Light Drifter

from PIL import Image

im = Image.open("hldata/east/test2.png")
new = im.resize((30, 19))
new.show()