from ColorFilter import ColorFilter as cf
from ImageProcessor import ImageProcessor as ip
import numpy as np
from PIL import Image

#array1 = np.random.randint(10, size=(2, 2, 3))
array1 = ip.load(path='../ex01/koala.jpg')
ip.display(cf.invert(array1))

ip.display(cf.to_blue(array1))
ip.display(cf.to_green(array1))
ip.display(cf.to_red(array1))
ip.display(cf.to_grayscale(array1, 'm'))
ip.display(cf.to_grayscale(array1, 'w'))
ip.display(cf.mean_blur(array1))
