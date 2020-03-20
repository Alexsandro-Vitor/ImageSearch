import argparse
from Search import search_image
import numpy as np

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-r', '--red', action='store_true',\
		help='Compares the red channel of the images (default %(default)s)')
	parser.add_argument('-g', '--green', action='store_true',\
		help='Compares the green channel of the images (default %(default)s)')
	parser.add_argument('-b', '--blue', action='store_true',\
		help='Compares the blue channel of the images (default %(default)s)')
	parser.add_argument('-a', '--alpha', action='store_true',\
		help='Compares the alpha channel of the images (default %(default)s)')
	parser.add_argument('image',\
		help='The image which will be compared to the images on <folder>')
	parser.add_argument('folder',\
		help='The folder containing the images to be compared with <image>')
	arguments = parser.parse_args()
	print(search_image(arguments))