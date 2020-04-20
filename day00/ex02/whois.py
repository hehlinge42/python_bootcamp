#!/usr/bin/python3

import sys

arg_list = sys.argv

if len(arg_list) == 2:
	nb = int(arg_list[1])
	str_to_print = "I'm "
	if nb == 0:
		str_to_print += "Zero."
	elif nb % 2 == 0:
		str_to_print += "Even."
	else:
		str_to_print += "Odd."
	print(str_to_print)
else:
	print("ERROR")
