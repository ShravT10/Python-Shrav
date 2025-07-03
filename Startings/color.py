import colorgram
import turtle as t
from turtle import Screen
import random
vaish = t.Turtle()
t.colormode(255)
vaish.speed(0)
x = -200
y = -100
vaish.teleport(x,y)
vaish.width(10)
end = 0

color_list = [(1, 30, 9), (121, 41, 95), (72, 21, 32), (238,72, 212), (220, 59, 81), 
(226, 100, 117), (93, 21, 1), (178, 170, 140), (151, 115, 92), 
(35, 26, 90), (6, 73, 154), (205, 91, 63), (168, 78, 129), (3, 28, 78), (1, 147, 64), 
(221, 218, 179), (4, 218, 220), (80, 179, 135), (130, 177, 157),
(81, 135, 110), (120, 164, 187), (11, 220, 213), (118, 36, 18), 
(243, 7, 205), (132, 209, 223)]

def art(x,y,end):
    if end <10:
        for i in range(10):
            vaish.teleport(x,y)
            vaish.color(random.choice(color_list))
            x += 30
            vaish.circle(2)
            
        y += 30
        x = -200
        end += 1
        art(x,y,end)

art(x,y,end)






my_screen = Screen()
my_screen.exitonclick()



# color = colorgram.extract('img.jpg',30)
# rgb = []
# for colors in color:
#     r = colors.rgb.r
#     g = colors.rgb.g
#     b = colors.rgb.b
#     new = ( r , b , g )
#     rgb.append(new)

# print(rgb)



