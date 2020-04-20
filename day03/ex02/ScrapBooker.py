import numpy as np

class ScrapBooker:
	
	def crop(array, dimensions, position=(0,0)):
	
		if dimensions[0] > array.shape[0] \
			or dimensions[1] > array.shape[1] \
			or (dimensions[0] + position[0] > array.shape[0]) \
			or (dimensions[1] + position[1] > array.shape[1]):
				print("Error: cannot make a bigger crop than the original picture")
				return
		ret  = array.copy()
		ret = ret[position[0]:position[0] + dimensions[0], position[1]:position[1] + dimensions[1]]
		return ret

	def thin(array, n, axis):
		if axis == 0:
			ret  = array.copy()
			ret = ret[:, ::n]
			return ret
		elif axis == 1:
			ret  = array.copy()
			ret = ret[::n, :]
			return ret
		else:
			print("Value error on the 'axis value'")
			
	def juxtapose(array: np.array, n: int, axis=0):
	
		if axis == 0 or axis == 1:
			return np.concatenate((array,)*n, axis=axis)
		else:
			print("Value error on the 'axis value'")

	def mosaic(array, dimensions):
		dim1 = ScrapBooker.juxtapose(array, dimensions[0], 0)
		return ScrapBooker.juxtapose(dim1, dimensions[1], 1)
