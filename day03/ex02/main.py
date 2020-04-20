from ScrapBooker import ScrapBooker as sb
from ImageProcessor import ImageProcessor as ip
import numpy as np
from PIL import Image

#array1 = np.random.randint(10, size=(10, 10))
array1 = ip.load(path='../ex01/koala.jpg')
print(array1)
crop1 = sb.crop(array1, (300, 450), (100, 200))
print("\nCropped!")
print(crop1)
ip.display(crop1)

print("\nThined1")
thin1 = sb.thin(array1, 2, 0)
print(thin1)
ip.display(thin1)
print("\nThined2")
thin2 = sb.thin(array1, 2, 1)
print(thin2)
ip.display(thin2)

print("\nJuxtaposed1")
j1 = sb.juxtapose(array1, 2, 0)
print(j1)
ip.display(j1)
print("\nJuxtaposed2")
j2 = sb.juxtapose(array1, 2, 1)
print(j2)
ip.display(j2)

print("\nMosaic")
m1 = sb.mosaic(array1, (10, 10))
print(m1)
ip.display(m1)
