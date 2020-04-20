import pandas as pd


def proportionBySport(df, year, sport, gender):
	df_sport = df[(df['Sex'] == gender) & (df['Year'] == year) & (df['Sport'] == sport)].drop_duplicates(subset='Name', keep='first')
	df_gender =  df[(df['Sex'] == gender) & (df['Year'] == year)].drop_duplicates(subset='Name', keep='first')
	return len(df_sport) / len(df_gender)
