import pandas


data = pandas.read_csv("data.csv")
gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray, cinnamon, black]
}
dataframe = pandas.DataFrame(data_dict)
dataframe.to_csv("count.csv")
