#!/usr/bin/python3

import sys

str_to_print = ""

arg_list = sys.argv
del arg_list[0]
arg_list.reverse()

for arg_str in arg_list:
	arg_str = arg_str[::-1]
	arg_str = arg_str.swapcase()
	str_to_print += arg_str
	str_to_print += " "

if len(arg_list) > 0:
	str_to_print = str_to_print[:-1]
	print(str_to_print)
