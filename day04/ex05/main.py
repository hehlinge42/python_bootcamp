from FileLoader import FileLoader
from HowManyMedalsByCountry import *

fl = FileLoader()
data = fl.load("../athlete_events.csv")
print(howManyMedalsByCountry(data, 'France'))
print(ref(data, 'France'))
