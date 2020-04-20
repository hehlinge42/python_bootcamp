from FileLoader import FileLoader
from HowManyMedals import howManyMedals as hmm

fl = FileLoader()
data = fl.load("../athlete_events.csv")
print(hmm(data, 'Kjetil Andr Aamodt'))
