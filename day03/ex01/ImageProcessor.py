from PIL import Image
from numpy import asarray

class ImageProcessor:

	def load(path):
		try:
			image = Image.open(path)
			data = asarray(image)
			print("Loading image of dimensions %d x %d" %(data.shape[0], data.shape[1]))
			return data
		except FileNotFoundError:
			print("File not found")

	def display(data):
		image = Image.fromarray(data)
		image.show()
