from FileLoader import FileLoader
from ProportionBySport import proportionBySport as pbs

fl = FileLoader()
data = fl.load("../athlete_events.csv")
perc = pbs(data, 2004, 'Tennis', 'F')
print(perc)
