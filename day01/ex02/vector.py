from check_vector_input import CheckVectorInput

class Vector:
	
	def __init__(self, arg):	
		check_vector = CheckVectorInput()
		check_vector.check_argument(arg)
		try:
			if check_vector.nb_errors != 0:
				raise ValueError
		except ValueError:
			print(str(check_vector))
		else:
			self.values = check_vector.values
			self.size = len(self.values)
	
	def __str__(self):
		return "The vector has %d values: %s\n" %(self.size, str(self.values))

	def __repr__(self):
		return __str__()

	def __add__(self, to_add):
		try:
			if not isinstance(to_add, (Vector, float, int)):
				raise ValueError
			if isinstance(to_add, Vector) and self.size != to_add.size:
				raise IndexError
		except ValueError:
			print("Invalid argument type: %s" %(type(to_add)))
		except IndexError:
			print("Both vectors must be of same size")
		else:
			float_list = []
			if isinstance(to_add, Vector):
				for i in range(0, self.size):
					float_list.append(self.values[i] + to_add.values[i])
			else:
				for value in self.values:
					float_list.append(value + to_add)
			return Vector(float_list)
	
	def __radd__(self, to_add):
		return self.__add__(to_add)

	def __sub__(self, to_sub):
		to_sub = to_sub * -1
		return self.__add__(to_sub)

	def __rsub__(self, to_sub):
		return self.__sub__(to_sub)

	def __truediv__(self, to_div):
		try:
			if not isinstance(to_div, (float, int)):
				raise ValueError
		except ValueError:
			print("Argument must be of type 'int' or 'float', not %s" %(type(to_div)))
		else:
			float_list = []
			for i in range(0, self.size):
				float_list.append(self.values[i] / float(to_div))
			return Vector(float_list)
				
	
	def __rtruediv__(self, to_div):
		return self.__truediv__(to_div)

	
	def __mul__(self, to_mul):
		try:
			if not isinstance(to_mul, (Vector, float, int)):
				raise ValueError
			if isinstance(to_mul, Vector) and self.size != to_mul.size:
				raise IndexError
		except ValueError:
			print("Invalid argument type: %s" %(type(to_mul)))
		except IndexError:
			print("Both vectors must be of same size")
		else:
			if isinstance(to_mul, Vector):
				dot_product = 0
				for i in range(0, self.size):
					dot_product += self.values[i] * to_mul.values[i]
				return dot_product
			else:
				float_list = []
				for value in self.values:
					float_list.append(value * float(to_mul))
				return Vector(float_list)

	def __rmul__(self, to_mul):
		return self.__to__mul(to_mul) 
