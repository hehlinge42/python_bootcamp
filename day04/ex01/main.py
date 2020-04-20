from FileLoader import FileLoader
from YoungestFellah import YoungestFellah as yf

fl = FileLoader()
data = fl.load("../athlete_events.csv")
print(yf.youngestFellah(data, 2004))
