cookbook = {
	'sandwich': (('ham', 'bread', 'cheese', 'tomatoes'), 'lunch', 10),
	'cake': (('flour', 'sugar', 'eggs'), 'dessert', 60),
	'salad': (('avocado', 'arugula', 'tomatoes', 'spinach'), 'lunch', 15),
}

def format_recipe(name_recipe, content):
	print("Recipe for %s:\nIngredients list: " %(name_recipe), end = '')
	print(content[0])
	print("To be eaten for %s.\nTakes %d minutes of cooking\n" %(content[1], content[2]))

def print_recipe(recipe_name):
	for key, value in cookbook.items():
		if key == recipe_name:
			format_recipe(key, value)

def print_cookbook():
	for key, value in cookbook.items():
		format_recipe(key, value)

def del_recipe(recipe_name):
	for key in list(cookbook):
		if key == recipe_name:
			del cookbook[key]

def add_recipe():
	recipe_name = input("Please enter the recipe's name: ")
	meal_type = input("Please enter the meal's type: ")
	prep_time = input("Please enter the time required to cook the recipe: ")
	ingredients = []
	ingredient = ""
	while ingredient != "Q" and ingredient != "q":
		ingredient = input("Add an ingredient, Q to stop: ")
		if ingredient != "Q" and ingredient != "q":
			ingredients.append(ingredient)
	cookbook[recipe_name] = (ingredients, meal_type, int(prep_time))

user_input = 0
while user_input != 5:
	user_input = input("""Please select an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit\n""")
	try:
		user_input = int(user_input)
	except:
		print("This option does not exist, please type the corresponding number.To exit, enter 5.")
	else:
		if user_input == 2 or user_input == 3:
			recipe_name = input("Please enter a recipe's name: ")
			if user_input == 2:
				del_recipe(recipe_name)
			else:
				print_recipe(recipe_name)
		elif user_input == 1:
			add_recipe()
		elif user_input == 4:
			print_cookbook()
		elif user_input != 5:
			print("This option does not exist, please type the corresponding number.To exit, enter 5.")

print("Cookbook closed.")

