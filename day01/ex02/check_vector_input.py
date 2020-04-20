class CheckVectorInput:

	def __init__(self):
		self.nb_errors = 0
		self.txt_error = ""
		self.values = []

	def add_error(self, error_details):
		self.nb_errors += 1
		if self.txt_error != "":
			self.txt_error += ", "
		self.txt_error += error_details

	def build_from_list(self, arg):
		for value in arg:
			try:
				if isinstance(value, float) == False and isinstance(value, int) == False:
					raise ValueError
			except ValueError:
				self.add_error("Values inside the 'list' argument must be of type 'float', not %s" %(type(value)))
			else:
				self.values.append(float(value))

	def build_from_int(self, arg):
		i = 0
		while i < arg:
			self.values.append(float(i))
			i += 1

	def build_from_tuple(self, arg):
		try:
			if len(arg) != 2:
				raise ValueError
			elif isinstance(arg[0], int) == False or isinstance(arg[1], int) == False:
				raise ValueError
		except:
			self.add_error("The tuple argument must contain exactly 2 'int'")
		else:
			i = min(arg)
			while i < max(arg):
				self.values.append(float(i))
				i += 1

	def __str__(self):
		formatted_error = "%d error(s) occurred at construction of Vector: " %self.nb_errors
		formatted_error += self.txt_error
		formatted_error += "\n"
		return formatted_error

	def check_argument(self, arg):
		try:
			if isinstance(arg, list) == True:
				self.build_from_list(arg)
			elif isinstance(arg, int) == True:
				self.build_from_int(arg)
			elif isinstance(arg, tuple) == True:
				self.build_from_tuple(arg)
			else:
				raise TypeError
		except TypeError:
			self.add_error("'values' must be of type 'int', 'list' or 'tuple', not '%s'" %(type(arg)))
