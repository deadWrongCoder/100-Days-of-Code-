import pandas


data = pandas.read_csv("weather.csv")
print(round(data["temp"].mean(), 1))
