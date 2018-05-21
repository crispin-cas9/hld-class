# HLD Classification
A convolutional neural net to classify screenshots from the video game Hyper Light Drifter

Hyper Light Drifter is a sci-fi action RPG video game with 2D pixel graphics that I like a lot. In HLD, the world is split into four visually distinct regions: North, East, South, and West. This network uses the extensive collection of screenshots I took while playing to learn to recognize these regions.

The vast majority of the code is adapted from this tutorial: https://www.pyimagesearch.com/2017/12/11/image-classification-with-keras-and-deep-learning/

When testing out the code for yourself, make sure to run lenet, then train_network, then test_network. There are many libraries or packages that need to be installed before running; make sure to check the imports at the top of each file to make sure you have everything. Also, the code should be run with python 3.

To run the files:
python3 train_network.py -d hldata -m hld.model
python3 test_network.py -m hld.model