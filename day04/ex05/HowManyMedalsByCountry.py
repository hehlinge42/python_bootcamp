import pandas as pd

def howManyMedalsByCountry(df, country):
	sub_df = df[(df['Team'] == country)]
	olympics = list(sub_df['Year'].drop_duplicates())
	medals_list = ['Gold', 'Silver', 'Bronze']
	ret = {}
	for year in olympics:
		ret[year] = {}
		year_medals = ret[year]
		for medal in medals_list:
			year_medals[medal[0]] = len(sub_df[(sub_df['Year'] == year) & (sub_df['Medal'] == medal)].drop_duplicates(subset='Event'))
	return ret
