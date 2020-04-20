import sys
import argparse

t = (19,42,21)

def format_list(*int_list):
	str_to_print = "The % d numbers are: " %(len(int_list[0]))
	i = 0
	for item in int_list[0]:
		i += 1
		str_to_print += "% d, " %(item)
	str_to_print = str_to_print[:-1]
	str_to_print = str_to_print[:-1]
	print(str_to_print)

arg_list = sys.argv
del(arg_list[0])
if (len(arg_list) == 0):
	format_list(t)
else:
	parser = argparse.ArgumentParser(description='Process a list of integers.')
	parser.add_argument('integers', metavar='N', type=int, nargs='+')
	args = parser.parse_args(arg_list)
	arg_list = args.integers
	format_list(arg_list)
