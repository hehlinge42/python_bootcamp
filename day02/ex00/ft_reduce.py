


def ft_reduce(function_to_apply, list_of_inputs):
i	try:
		if (not isinstance(list_of_inputs, list) and not isinstance(list_of_inputs, tuple)) or not hasattr(function_to_apply, '__call__'):
			raise TypeError
	except TypeError:
		print("Error: bad input type")
	else:
		elem = list_of_inputs[0]
		for next_elem in list_of_inputs[1:]:
			elem = function_to_apply(elem, next_item)
		return elem
