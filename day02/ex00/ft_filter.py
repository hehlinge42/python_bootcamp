def ft_filter(function_to_apply, list_of_inputs):
	try:
		if (not isinstance(list_of_inputs, list) and not isinstance(list_of_inputs, tuple)) or not hasattr(function_to_apply, '__call__'):
			raise TypeError
	except TypeError:
		print("Error: bad input type")
	else:
		result = []
		for elem in list_of_inputs:
			if function_to_apply(elem) == True:
				result.append(elem)
		return result


# function that filters vowels 
def fun(variable): 
    letters = ['a', 'e', 'i', 'o', 'u'] 
    if (variable in letters): 
        return True
    else: 
        return False
  
  
# sequence 
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
print(ft_filter(fun, sequence)) 
