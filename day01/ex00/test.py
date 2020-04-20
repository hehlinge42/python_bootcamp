from recipe import Recipe
from book import Book

name = "Chicken"
cooking_lvl = 2
cooking_time = 30
ingredients = ["chicken", "sauce", "fries"]
description = "chicken with sauce and fries"
recipe_type = "lunch"

print("CHECKING BAD RECIPES")
#ERROR IN NAME
name = 0
try:
	invalid_name = Recipe(name, cooking_lvl, cooking_time, ingredients, description, recipe_type)
except:
	pass
	
#ERROR IN COOKING_LVL
try:
	cooking_lvl = "poor"
	invalid_lvl = Recipe(name, cooking_lvl, cooking_time, ingredients, description, recipe_type)
except:
	pass

#ERROR IN COOKING_TIME
try:
	cooking_time = "long"
	invalid_time = Recipe(name, cooking_lvl, cooking_time, ingredients, description, recipe_type)
except:
	pass

#ERROR IN INGREDIENTS
try:
	ingredients = 4
	invalid_ingredients = Recipe(name, cooking_lvl, cooking_time, ingredients, description, recipe_type)
except:
	pass

#ERROR IN INGREDIENT
try:
	ingredients = [1, 2]
	invalid_ingredient = Recipe(name, cooking_lvl, cooking_time, ingredients, description, recipe_type)
except:
	pass

#ERROR IN DESCRIPTION
try:
	description = ["description"]
	invalid_description = Recipe(name, cooking_lvl, cooking_time, ingredients, description, recipe_type)
except:
	pass

#ERROR IN RECIPE_TYPE
try:
	recipe_type = "breakfast"
	invalid_type = Recipe(name, cooking_lvl, cooking_time, ingredients, description, recipe_type)
	recipe_type = 4
	invalid_type = Recipe(name, cooking_lvl, cooking_time, ingredients, description, recipe_type)
except:
	pass

print("Checking valid recipes")
#VALID TESTS
try:
	name = "Chicken"
	cooking_lvl = 2
	cooking_time = 30
	ingredients = ["chicken", "sauce", "fries"]
	description = "chicken with sauce and fries"
	recipe_type = "lunch"
	lunch_recipe = Recipe(name, cooking_lvl, cooking_time, ingredients, description, recipe_type)
	print(str(lunch_recipe))

	name = "Salad"
	cooking_lvl = 1
	cooking_time = 5
	ingredients = ["tomatoes", "mozzarella"]
	description = "tomatoes and mozzarella"
	recipe_type = "starter"
	starter_recipe = Recipe(name, cooking_lvl, cooking_time, ingredients, description, recipe_type)
	print(str(starter_recipe))

	name = "Cookies"
	cooking_lvl = 2
	cooking_time = 30
	ingredients = ["flour", "egg", "sugar", "chocolate"]
	description = "chocolat chips cookies"
	recipe_type = "dessert"
	dessert_recipe = Recipe(name, cooking_lvl, cooking_time, ingredients, description, recipe_type)
	print(str(starter_recipe))

	print("CREATING BOOK")
	#CREATING BOOKS
	recipes_list = [lunch_recipe, starter_recipe, dessert_recipe]
	book_from_list = Book("Book from list of recipes", recipes_list)
	print(str(book_from_list))
	recipes_dict = {
		"starter": [starter_recipe],
		"lunch": [lunch_recipe],
		"dessert": [dessert_recipe]
	}
	book_from_dict = Book("Book from dict of recipes", recipes_dict)
	print(str(book_from_dict))


	book_from_list.get_recipe_by_name("Chicken")
	name = "Cake"
	cooking_lvl = 2
	cooking_time = 30
	ingredients = ["flour", "egg", "sugar", "bananas"]
	description = "banana bread"
	recipe_type = "dessert"
	extra_recipe = Recipe(name, cooking_lvl, cooking_time, ingredients, description, recipe_type)
	book_from_list.add_recipe(1)
	book_from_list.add_recipe(extra_recipe)
	desserts_list = book_from_list.get_recipes_by_types("dessert")
	for dessert in desserts_list:
		print(str(dessert))
except:
	pass
