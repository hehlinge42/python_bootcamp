import numpy as np

class NumPyCreator:

	def from_list(self, lst: 'list', dtype=None) -> np.array:
		return np.asarray(lst).astype(dtype)

	def from_tuple(self, tpl: 'tuple', dtype=None) -> np.array:
		return np.asarray(tpl).astype(dtype)

	def from_iterable(self, itr: 'iterable', dtype=None) -> np.array:
		return np.asarray(itr).astype(dtype)

	def from_shape(self, shape: 'tuple', value, dtype=None) -> np.array:
		return np.zeros(shape, value).astype(dtype)

	def random(self, shape: 'tuple', dtype=None) ->np.array:
		return np.random.rand(shape[0], shape[1]).astype(dtype)
		
	def identity(self, n: 'int', dtype=None):
		return np.identity(n, dtype=dtype)
