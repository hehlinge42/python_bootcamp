import sys
import argparse

arg_list = sys.argv
del arg_list[0]

if len(arg_list) == 0:
	print("Usage: python operations.py\nExample:\n\tpython operations.py 10 3")
elif len(arg_list) > 2:
	print("InputError: too many arguments")
else:
	parser = argparse.ArgumentParser(description='Process 2 integers.')
	parser.add_argument('integers', metavar='N', type=int, nargs='+')

	args = parser.parse_args(arg_list)
	arg_list = args.integers

	if len(arg_list) != 2:
		print("InputError: only numbers")
	else:
		print("Sum: % d" %(arg_list[0] + arg_list[1]))
		print("Difference: % d" %(arg_list[0] - arg_list[1]))
		print("Product: % d" %(arg_list[0] * arg_list[1]))
		if arg_list[1] == 0:
			print("Quotient: ERROR (div by zero)")
			print("Remainder: ERROR (div by zero)")
		else:
			print("Quotient: % f" %(float(arg_list[0] / arg_list[1])))
			print("Remainder: % d" %(arg_list[0] % arg_list[1]))
