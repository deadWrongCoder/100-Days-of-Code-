import pandas


data = pandas.read_csv("weather.csv")
print("Max value is ", data["temp"].max())
print("Mean value is ", round(data["temp"].mean(), 1))
print(data[data.temp == data.temp.max()])
