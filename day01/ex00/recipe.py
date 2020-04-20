from recipe_test_input import RecipeTestInput

class Recipe:

	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		
		error = RecipeTestInput()
		error.check_input(name, cooking_lvl, cooking_time, ingredients, description, recipe_type)	
		try:
			if error._get_nb_errors() != 0:
				raise ValueError(str(error))
		except ValueError:
			print(str(error))
		else:
			self.name = name
			self.cooking_lvl = cooking_lvl
			self.cooking_time = cooking_time
			self.ingredients = ingredients
			self.description = description
			self.recipe_type = recipe_type

	def __str__(self):
		
		formatted_str = "Recipe for %s:\n" %(self.name)
		formatted_str += "Requires a cooking level of %d / 5\n" %(self.cooking_lvl)
		formatted_str += "Takes %d minutes of preparation\n" %(self.cooking_time)
		formatted_str += "List of ingredients: %s\n" %(str(self.ingredients))
		formatted_str += "Full description: %s\n" %(self.description)
		formatted_str += "To be eaten for %s.\n" %(self.recipe_type)
		return formatted_str

