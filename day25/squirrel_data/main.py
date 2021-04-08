import pandas


data = pandas.read_csv("squirrel_count.csv")
data_dict = data.to_dict()

gray_squirrels = data[data["Primary Fur Color"] == "Gray" ]
black_squirrels = data[data["Primary Fur Color"] == "Black" ]
cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon" ]

new_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(gray_squirrels), len(cinnamon_squirrels), len(black_squirrels)]

}
data_out = pandas.DataFrame(new_dict)

data_out.to_csv("squirrel_colors.csv")