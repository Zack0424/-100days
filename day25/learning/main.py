import csv
import pandas
# with open("weather_data.csv") as f:
#     temperatures = []
#     data = csv.reader(f)
#     for row in data:
#         if row[1].isnumeric():
#             temperatures.append(int(row[1]))
#     print(temperatures)

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
print(data_dict)

# Avg
# temp_list = data["temp"].to_list()
# temp_avg = sum(temp_list) / len(temp_list)
# print(temp_avg)
print(data["temp"].mean())

# print(data["temp"].max())
# # Get data in columns
# print(data.condition)
# print(data["condition"])

# Get data in row

print(data[data.day == "Monday"])

print(data[data.temp == data.temp.max() ])

monday = data[data.day == "Monday"]

monday_temp = int(monday.temp)
monday_temp_f = monday_temp * 9/5 +32
print(monday_temp_f)

# Create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

