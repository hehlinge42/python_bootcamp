import numpy as np

class ColorFilter:

	def invert(array):
		return 255 - array

	def to_color(array, color):
		ret = array.copy()
		for line in ret:
			for col in line:
				i = 0
				while i < 3:
					if i != color:
						col[i] = 0
					i += 1
		return ret

	def to_blue(array):
		return ColorFilter.to_color(array, 2)

	def to_green(array):
		return ColorFilter.to_color(array, 1)

	def to_red(array):
		return ColorFilter.to_color(array, 0)

	def to_grayscale(array, option='w'):
		if option in ['mean', 'm']:
			ret = array.copy()
			ret.setflags(write=1)
			for line in ret:
				for pixel in line:
					pixel[::1] = np.sum(pixel[::1] / 3)
			return ret
		elif option in ['w', 'weighted']:
			ret = array.copy()
			ret.setflags(write=1)
			coeff = [0.299, 0.587, 0.114]
			for line in ret:
				for pixel in line:
					pixel[::1] = np.dot(pixel[::1], [0.299, 0.587, 0.114])
			return ret
