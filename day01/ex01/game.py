

class GotCharacter:

	def __init__(self, first_name):

		try:
			if isinstance(first_name, str) == False:
				raise ValueError
		except ValueError:
			print("'first_name' attribute must be of type 'str', not %s" %(type(first_name)))
		else:
			self.first_name = first_name
			self.is_alive = True


class Stark(GotCharacter):

	def __init__(self, first_name):
		try:
			if isinstance(first_name, str) == False:
				raise ValueError
		except ValueError:
			print("'first_name' attribute must be of type 'str', not %s" %(type(first_name)))
		else:
			super().__init__(first_name)
			self.family_name = "Stark"
			self.house_words = "Winter is Coming"
			self.__doc__ = "A class representing the Stark family. Or when bad things happen to good people."

	def die(self):
		self.is_alive = False

	def print_house_words(self):
		print(self.house_words)
