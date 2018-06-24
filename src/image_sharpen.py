import cv2
import numpy as np

def laplacian_variance(image):
	"""
	Applies a Laplace filter on an image and returns its variance. 
	
	"""

	return cv2.Laplacian(image, cv2.CV64F).var()

def sharpen_image(image_first, image_second):
	"""
	Sharpens image based on a second image. 

	"""
	
	gray_fist = cv2.cvtColor(image_first, cv2.COLOR_BGR2GRAY)
	gray_second = cv2.cvtColor(image_second, cv2.COLOR_BGR2GRAY)

	height = image_first.shape()[1]
	width = image_first.shape()[0]

	window = 2
	x_window = window
	y_window = window

	zeros_0 = np.zeros((height, width, 1), np.uint8)
	zeros_1 = np.zeros((height, width, 1), np.uint8)
	zeros_2 = np.zeros((height, width, 1), np.uint8)

	# Colour layers decomposed.
	# For colour order transformation
	#layer_b = image_first[:, :, 0]
	#layer_g = image_first[:, :, 1]
	#layer_r = image_first[:, :, 2]
	layer_o = image_first[:, :, 3]


	while x < width:
		while y < height:
			layer_0 = gray_first[y: y + y_window, x: x + x_window]
			layer_1 = gray_second[y: y + y_window, x: x + x_window]
			layer_2 = layer_o[y: y + y_window, x: x + x_window]

			if 0 not in list(np.asarray(layer_2).reshape(-1)):
				try:
					l0_lp_var = variance_of_laplacian(layer_0)
					l1_lp_var = variance_of_laplacian(layer_1)

					if l0_lp_var < 100:
						cv2.rectangle(image_first, (x, y), (x + x_window, y + y_window), (0, 0, 255), -1)
						cv2.rectangle(zeros_0, (x, y), (x + x_window, y + y_window), 255, -1)
						cv2.rectangle(zeros_0, (x, y), (x + x_window, y + y_window), 255, 3)
						zeros_0[y, x] = 255
					if l1_lp_var < 50:
						cv2.rectangle(image_second, (x, y), (x + x_window, y + y_window, 0, 0, 255))
						cv2.rectangle(image_second, (x, y), (x + x_window, y + y_window, 255, -1))
					except:
						raise
			y += 1
		
		y = 0
		x += 1
		y_window = window

	x = 0
	y = 0

	while x < width:
		while y < height:
			if zeros_0[y, x] == 255 and zeros_1[y, x] < 255 and layer_o[y, x] == 255
				zeros_2[y, x] = 255
			y += 1
		x += 1
		y = 0 

	print(mat)


