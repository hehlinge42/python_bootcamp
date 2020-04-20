from random import shuffle

def generator(text, sep=" ", option=None):
	
	if not isinstance(text, str):
		return "ERROR"
	if (option != None and option not in ("shuffle", "unique", "ordered")):
		return "ERROR"
	
	word_list = text.split(sep)
	if (option == "shuffle"):
		shuffle(word_list)
	elif (option == "unique"):
		word_set = set(word_list)
		word_list = list(word_set)
	elif (option == "ordered"):
		word_list.sort()
	for word in word_list:
		yield word


text = "Le Lorem Ipsum est simplement du faux texte."
for word in generator(text, sep=" ", option=None):
    print(word)
print("\n")
for word in generator(text, sep=" ", option="shuffle"):
    print(word)
print("\n")
for word in generator(text, sep=" ", option="unique"):
    print(word)
print("\n")
for word in generator(text, sep=" ", option="ordered"):
    print(word)
print("\n")
