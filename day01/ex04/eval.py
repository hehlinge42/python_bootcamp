class Evaluator:
	
	@staticmethod
	def zip_evaluate(coeff, words):
		if not isinstance(coeff, list) or not isinstance(words, list) or len(coeff) != len(words):
			return -1
		result = 0
		for word, coeff in zip(words, coeff):
			result += len(word) * coeff
		return result

	@staticmethod
	def enumerate_evaluate(coeff, words):
		if not isinstance(words, list) or not isinstance(coeff, list) or len(coeff) != len(words):
			return -1
		result = 0
		for i, word in enumerate(words):
			result += len(word) * coeff[i]
		return result
