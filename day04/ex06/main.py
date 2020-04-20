from FileLoader import FileLoader
from MyPlotLib import MyPlotLib

fl = FileLoader()
data = fl.load("../athlete_events.csv")

pl = MyPlotLib()
pl.histogram(data, ["Height", "Weight"])
pl.density(data, ["Weight", "Height"])
pl.pair_plot(data, ["Weight", "Height"])
pl.box_plot(data, ["Weight", "Height"])
