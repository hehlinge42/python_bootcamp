import sys

MORSE_CODE_DICT = {
	'A':'.-',
	'B':'-...', 
    'C':'-.-.',
	'D':'-..',
	'E':'.', 
    'F':'..-.',
	'G':'--.',
	'H':'....', 
    'I':'..',
	'J':'.---',
	'K':'-.-', 
    'L':'.-..',
	'M':'--',
	'N':'-.', 
    'O':'---',
	'P':'.--.',
	'Q':'--.-', 
	'R':'.-.',
	'S':'...',
	'T':'-', 
	'U':'..-',
	'V':'...-',
	'W':'.--', 
    'X':'-..-',
	'Y':'-.--',
	'Z':'--..', 
    '1':'.----',
	'2':'..---',
	'3':'...--', 
    '4':'....-',
	'5':'.....',
	'6':'-....', 
    '7':'--...',
	'8':'---..',
	'9':'----.', 
    '0':'-----',
	', ':'--..--',
	'.':'.-.-.-', 
    '?':'..--..',
	'/':'-..-.',
	'-':'-....-', 
    '(':'-.--.',
	 ')':'-.--.-',
	 ' ':'/ '
}

args = sys.argv
del(args[0])

str_to_print = ""

for string in args:
	for character in string:
		if character.islower():
			character = character.upper()
		if character in MORSE_CODE_DICT:
			str_to_print += MORSE_CODE_DICT[character]
			str_to_print += " "
		else:
			print("ERROR: Bad char: '%s'" %character)
	str_to_print += MORSE_CODE_DICT[' ']

str_to_print = str_to_print[:-3]
print(str_to_print)
