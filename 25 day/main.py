import pandas


data = pandas.read_csv("weather.csv")
temp_list = data["temp"].to_list()
sum = 0
for temp in temp_list:
    sum += temp
average_temp = sum / len (temp_list)
print(round(average_temp, 1))
