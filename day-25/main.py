# # import csv

# # with open("./weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     print(data)
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))

# #     print(temperatures)

# import pandas

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# # print(data_dict)

# # Converts data to series/list
# # temp_list = data["temp"].to_list()
# # print(temp_list)

# # print(data["temp"].mean())
# # print(data["temp"].max())

# # print(data[data.day == "Monday"])
# # print(data[data["temp"] == data.temp.max()])

# monday = data[data.day == "Monday"]
# print((monday.temp.item() * 9) / 5 + 32)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]
fur_color_data = pandas.DataFrame(fur_color.value_counts())
fur_color_data.to_csv("new_squirrel_count.csv")
