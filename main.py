import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel_count = len(data[data["Primary Fur Color" == "Gray"]])
cinnamon_squirrel_count = len(data[data["Primary Fur Color" == "Cinnamon"]])
black_squirrel_count = len(data[data["Primary Fur Color" == "Black"]])
