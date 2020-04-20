def ft_map(function_to_apply, list_of_inputs):
	try:
		if (not isinstance(list_of_inputs, list) and not isinstance(list_of_inputs, tuple)) or not hasattr(function_to_apply, '__call__'):
			raise TypeError
	except TypeError:
		print("Error: bad input type")
	else:
		result = []
		for elem in list_of_inputs:
			result.append(function_to_apply(elem))
		return result

# Return double of n 
def addition(n):
	return n + n 

# We double all numbers using map() 
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(list(result)) 
