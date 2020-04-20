from recipe import Recipe

class BookTestInput:

	def __init__(self):
		self.nb_errors = 0
		self.txt_error = ""
		self.starter_recipes = []
		self.lunch_recipes = []
		self.dessert_recipes = []
		self.recipes_dict = {}

	def add_error(self, error_details):
		self.nb_errors += 1
		if self.txt_error != "":
			self.txt_error += ", "
		self.txt_error += error_details

	def check_name(self, name):	
		if isinstance(name, str) == False:
			self.add_error("'name' attribute must be of type 'str', not %s" %(type(name)))
	
	def check_recipes_list(self, recipes):
		for recipe in recipes:
			if isinstance(recipe, Recipe) == False:
				self.add_error("'recipes' must be of type 'Recipe', not %s" %(type(recipe)))
			else:
				if recipe.recipe_type == "starter":
					self.starter_recipes.append(recipe)
				elif recipe.recipe_type == "lunch":
					self.lunch_recipes.append(recipe)
				elif recipe.recipe_type == "dessert":
					self.dessert_recipes.append(recipe)
				else:
					self.add_error("recipe %s has invalid attribute 'recipe_type': '%s'" %(recipe.name, recipe.recipe_type))

	def check_recipes_dict(self, recipes):
		for key, value in recipes.items():
			if key != "starter" and key != "lunch" and key != "dessert":
				self.add_error("recipe %s has invalid attribute 'recipe_type': '%s'" %(value.name, key))

	def check_recipes(self, recipes):
		if isinstance(recipes, list):
			self.check_recipes_list(recipes)
		elif isinstance(recipes, dict):
			self.check_recipes_dict(recipes)
		else:
			self.add_error("'recipes' attribute must be of type 'list' or 'dict', not %s" %(type(recipes)))

	def _get_nb_errors(self):
		return self.nb_errors

	def check_input(self, name, recipes):
		
		self.check_name(name)
		self.check_recipes(recipes)
		if self.nb_errors == 0 and isinstance(recipes, list):
			self.recipes_dict["starter"] = self.starter_recipes
			self.recipes_dict["lunch"] = self.lunch_recipes
			self.recipes_dict["dessert"] = self.dessert_recipes
		elif self.nb_errors == 0 and isinstance(recipes, dict):
			self.recipes_dict = recipes
