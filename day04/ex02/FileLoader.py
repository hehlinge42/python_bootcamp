import pandas as pd 

class FileLoader:
	
	def load(self, path):
		data = pd.read_csv(path)
		print("Loading a file of dimensions %d x %d" %(data.shape[0], data.shape[1]))
		return data
	
	def display(self, df, n):
		if n > 0:
			print(df.head(n))
		else:
			print(df.tail(-n))
