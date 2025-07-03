import pandas

sdata = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

cinnamon = len(sdata[sdata["Primary Fur Color"] == "Cinnamon"])
black = len(sdata[sdata["Primary Fur Color"] == "Black"])
gray = len(sdata[sdata["Primary Fur Color"] == "Gray"])

data_dict = {
    "Color" : ["Gray" , "Black" , "Cinnamon"],
    "Count" : [gray , black , cinnamon]
}

new_sdata = pandas.DataFrame(data_dict)
new_sdata.to_csv("Squirrel_min.csv")
