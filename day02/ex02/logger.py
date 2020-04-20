from time import time
from random import randint

def log(function):
	#Measures exec time of a function

	def modified_func(*args, **kwargs):	
		time_bef = time()
		ret = function(*args, **kwargs)
		time_aft = time()
		with open('machine.log', 'a+') as f:
			f.write(f'(hehlinge)Running: {function.__name__} [ exec-time =  {time_aft - time_bef:.3f} ms ]\n')
		return ret
	return modified_func
