import pandas as pd

class YoungestFellah:

	def youngestFellah(df, year):
		return {'f': df['Age'][(df['Sex'] == 'F') & (df['Year'] == year)].min(),
              'm': df['Age'][(df['Sex'] == 'M') & (df['Year'] == year)].min()}
