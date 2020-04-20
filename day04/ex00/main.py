from FileLoader import FileLoader

fl = FileLoader()
data = fl.load("../athlete_events.csv")
fl.display(data, 10)
fl.display(data, -10)
