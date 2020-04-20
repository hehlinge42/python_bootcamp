import pandas as pd

class SpatioTemporalData:

	def __init__(self, df):
		self.df = df

	def when(self, location):
		df = self.df
		return list(df['Year'][(df['City'] == location)].drop_duplicates())

	def where(self, date):
		df = self.df
		return list(df['City'][(df['Year'] == date)].drop_duplicates())
