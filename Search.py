import numpy as np
import cv2 as cv
import glob
import os

def compare_images(img, folder_img_path, args):
	folder_img = cv.imread(folder_img_path, cv.IMREAD_UNCHANGED)
	comparison = img - folder_img
	print((comparison[:32, :24, 3]/255).astype(int))
	results = np.sum(comparison, axis=(0,1))
	results_filter = [args.blue, args.green, args.red, args.alpha]
	return np.sum(results, where=results_filter)

def search_image(args):
	img = cv.imread(args.image, cv.IMREAD_UNCHANGED)
	folder_img_paths = glob.glob(os.path.join(args.folder, '*.png'), recursive=True)
	image_differences = [compare_images(img, img_path, args) for img_path in folder_img_paths]
	min_difference_image = np.argmin(image_differences)
	return folder_img_paths[min_difference_image]