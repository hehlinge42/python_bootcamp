from recipe import Recipe
from book_test_input import BookTestInput
from datetime import datetime

class Book:

	def __init__(self, name, recipes_list):
		
		test_input = BookTestInput()
		test_input.check_input(name, recipes_list)
		
		try:
			if test_input._get_nb_errors() != 0:
				raise ValueError(str(test_input))
		except ValueError:
			print(str(test_input))
		else:
			now = datetime.now()
			self.name = name
			self.last_update = now
			self.creation_date = now
			self.recipes_list = test_input.recipes_dict


	def __str__(self):
		formatted_input = "The book '%s' was created on %s and last updated on %s\n" %(self.name, str(self.creation_date), str(self.last_update))
		formatted_input += "It has %d starters, %d lunches and %d desserts\n" %(len(self.recipes_list["starter"]), len(self.recipes_list["lunch"]), len(self.recipes_list["dessert"]))
		return formatted_input

	def get_recipe_by_name(self, name):
		tmp_dict = self.recipes_list
		for recipes_by_type in self.recipes_list.values():
			for recipe in recipes_by_type:
				if recipe.name == name:
					print(str(recipe))
					return recipe
		return None

	def get_recipes_by_types(self, recipe_type):
		if recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert":
			print("Invalid 'recipe_type': %s" %(recipe_type))
			return None
		else:
			return self.recipes_list[recipe_type]
			
	def add_recipe(self, recipe):
		try:
			if isinstance(recipe, Recipe) == False:
				raise ValueError("Argument of 'add_recipe' must be of type 'Recipe', not %s" %(type(recipe)))
			elif recipe.recipe_type != "starter" and recipe.recipe_type != "lunch" and recipe.recipe_type != "dessert":
				raise ValueError("Invalid field 'recipe_type': %s" %(recipe.recipe_type))
		except ValueError:
			pass
		else:
			self.recipes_list[recipe.recipe_type].append(recipe)
			now = datetime.now()
			self.last_update = now
