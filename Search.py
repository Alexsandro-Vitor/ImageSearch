import numpy as np
import cv2 as cv
import glob
import os

BLUE_CHANNEL = 0
GREEN_CHANNEL = 1
RED_CHANNEL = 2
WHITE_CHANNEL = 3

def get_treated_image(img_path):
	raw_img = cv.imread(img_path, cv.IMREAD_UNCHANGED)
	shape = raw_img.shape
	output = np.zeros((shape[0], shape[1], 4), dtype=np.int16)
	output[:, :, -1] = np.tile(255, shape[:2])
	output[:, :, :raw_img.shape[2]] = raw_img
	return output

def compare_images(img, folder_img_path, args):
	folder_img = get_treated_image(folder_img_path)
	comparison = np.absolute(img - folder_img)
	results = np.sum(comparison, axis=(0,1))
	results_filter = [args.blue, args.green, args.red, args.alpha]
	return np.sum(results, where=results_filter)

def search_image(args):
	img = get_treated_image(args.image)

	folder_img_paths = glob.glob(os.path.join(args.folder, '*.png'), recursive=True)
	image_differences = [compare_images(img, img_path, args) for img_path in folder_img_paths]
	min_difference_image = np.argmin(image_differences)
	return folder_img_paths[min_difference_image]