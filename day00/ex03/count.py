import string

def text_analyzer(*arg):
	
	arg_list = list(arg)

	if len(arg_list) > 1:
		print("Too many arguments")
	elif len(arg_list) == 0:
		user_input = input("What is the text to analyse?: ")
		text_analyzer(user_input)
	else:
		str = arg_list[0]
		nb_chars = 0
		nb_upper = 0
		nb_lower = 0
		nb_punct = 0
		nb_spaces = 0
		for char in str:
			nb_chars += 1
			if char.isspace():
				nb_spaces += 1
			elif char in string.punctuation:
				nb_punct += 1
			elif char.islower():
				nb_lower += 1
			elif char.isupper():
				nb_upper += 1

		print("The text contains % d characters:" %(nb_chars))
		print("- % d upper letters" %(nb_upper))
		print("- % d lower letters" %(nb_lower))
		print("- % d punctuation marks" %(nb_punct))
		print("- % d spaces" %(nb_spaces))
