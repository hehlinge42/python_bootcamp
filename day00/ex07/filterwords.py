import sys
import string

args = sys.argv
del(args[0])

if len(args) != 2:
	print("ERROR: number of arguments is not 2")
else:
	try:
		max_size = int(args[1])
	except:
		print("ERROR: please enter an integer as 2nd argument")
	else:
		if all(x.isalpha() or x.isspace() or x in string.punctuation for x in args[0]):
			str_list = args[0].split();
			str_list = [word for word in str_list if len(word) > max_size]
			print(str_list)
		else:
			print("ERROR: please enter a alphabetical string as 1st argument (spaces and punctuation accepted)")
