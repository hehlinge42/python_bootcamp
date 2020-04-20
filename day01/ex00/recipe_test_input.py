class RecipeTestInput:

	def __init__(self):
		self.nb_errors = 0
		self.txt_error = ""

	def add_error(self, error_details):
		self.nb_errors += 1
		if self.txt_error != "":
			self.txt_error += ", "
		self.txt_error += error_details

	def check_name(self, name):	
		if isinstance(name, str) == False:
			self.add_error("'name' attribute must be of type 'str', not %s" %(type(name)))
	
	def check_cooking_lvl(self, cooking_lvl):
		if isinstance(cooking_lvl, int) == False:
			self.add_error("'cooking_lvl' attribute must be of type 'int', not %s" %type(cooking_lvl))
		elif cooking_lvl < 1 or cooking_lvl > 5:
			self.add_error("'cooking_lvl' attribute must be comprised between 1 and 5, not %d" %cooking_lvl)

	def check_cooking_time(self, cooking_time):
		if isinstance(cooking_time, int) == False:
			self.add_error("'cooking_time' attribute must be of type 'int', not %s" %(type(cooking_time)))
		elif cooking_time < 0:
			self.add_error("'cooking_time' attribute must be positive, not %d" %(cooking_time))
	
	def check_ingredients(self, ingredients):
		if isinstance(ingredients, list) == False:
			self.add_error("'ingredients' attribute must be of type 'list', not %s" %(type(ingredients)))
		else:
			if len(ingredients) == 0:
				self.add_error("'ingredients' cannot be empty")
			for ingredient in ingredients:
				if isinstance(ingredient, str) == False:
					self.add_error("ingredients must be of type 'str', not %s" %(type(ingredient)))
	
	def check_description(self, description):
		if isinstance(description, str) == False:
			self.add_error("'description' attribute must be of type 'str', not %s" %(type(description)))
	
	def check_recipe_type(self, recipe_type):
		if isinstance(recipe_type, str) == False:
			self.add_error("'recipe_type' attribute must be of type 'str', not %s" %(type(recipe_type)))
		elif recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert":
			self.add_error("'recipe_type' attributed must be either 'starter', 'lunch', or 'dessert', not %s" %recipe_type)

	def __str__(self):
		
		formatted_error = "%d errors occurred at construction of Recipe: " %self.nb_errors
		formatted_error += self.txt_error
		formatted_error += "\n"
		return formatted_error
		
	def _get_nb_errors(self):
		return self.nb_errors

	def check_input(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		
		self.check_name(name)
		self.check_cooking_lvl(cooking_lvl)
		self.check_cooking_time(cooking_time)
		self.check_ingredients(ingredients)
		self.check_description(description)
		self.check_recipe_type(recipe_type)
