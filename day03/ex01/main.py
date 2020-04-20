from ImageProcessor import ImageProcessor as ip

try:
	data = ip.load('koala.jpg')
	print(data)

	ip.display(data)

	ip.load('none.jpg')

except:
	pass
