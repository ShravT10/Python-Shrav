# with open("weather_data.csv") as data:
#     con = data.readlines()
#     print(con)

# import csv

# with open("weather_data.csv") as data:
#     data_list = csv.reader(data)
#     temp = []
#     for i in data_list:
#         if i[1] == "temp":
#             pass
#         else:
#             temp.append((int(i[1])))
# print(temp)

import pandas

# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_html()
# # print(data_dict)


# flist = data["temp"].to_list()
# a = 0
# for i in flist:
#     a+=i
# print(f"Average is : {round(a/len(flist),2)}")

# print(f"Average is : {data['temp'].mean()}")

# max element
# print(data['temp'].max())

# getting hold of a coloumn
# print(data.condition) #works same 
# print(data["condition"])

# getting hold of a row
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Sunday"]
# temp = monday.temp[0]
# print(temp)

# data_dict = {
#     "students" : ["amy","shrav","psn"] ,
#     "scores" : [50 , 60 , 70]
# }

# data = pandas.DataFrame(data_dict)
# # print(data)
# new_data = data.to_csv("New_csv.csv")

# csvdata = pandas.read_csv("New_csv.csv")

# csvtohtml = csvdata.to_html("new.html")
# print(csvtohtml)

