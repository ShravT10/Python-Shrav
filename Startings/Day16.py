
from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Games",["Valorant","Genshin Impact","DOTA 2"])
table.add_column("Type",["FPS","Gacha","MOBA"])
table.align="l"
print(table)
print(table.align)
