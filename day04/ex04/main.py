from FileLoader import FileLoader
from SpatioTemporalData import SpatioTemporalData as STD

fl = FileLoader()
data = fl.load("../athlete_events.csv")
std = STD(data)
print(std.when('Paris'))
print(std.where(2016))
