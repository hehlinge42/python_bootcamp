import sys
import argparse

t = (3,30,2019,9,25)

def format_date(int_list):
	print("%d/%d/%d %d:%d" %(int_list[3], int_list[4], int_list[2], int_list[0], int_list[1]))

arg_list = sys.argv
del(arg_list[0])
if (len(arg_list) == 0):
	format_date(t)
else:
	parser = argparse.ArgumentParser(description='Process a list of integers.')
	parser.add_argument('integers', metavar='N', type=int, nargs='+')
	args = parser.parse_args(arg_list)
	arg_list = args.integers
	if len(arg_list) == 5:
		format_date(arg_list)
	else:
		print("InputError: 5 integers required")
	
