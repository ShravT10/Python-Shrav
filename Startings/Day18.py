import turtle as t 
from turtle import Screen
import random

vaishuqt = t.Turtle()

t.colormode(255)
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0 ,90 , 180 , 270]
vaishuqt.speed(0)
def color_picker():
    a = random.randint(0,255)
    return a 
for _ in range(60):
    vaishuqt.circle(100)
    vaishuqt.left(6)
    vaishuqt.color((color_picker(),color_picker(),color_picker()))













my_screen = Screen()
my_screen.exitonclick()




######## ALL SHAPES GENERATOR ########

# vaishuqt.shape("turtle")
# vaishuqt.color("DodgerBlue")
# shapes = [3,4,5,6,7,8,9]
# side = len(shapes)

# for _ in shapes:
#     vaishuqt.color(random.choice(colours))
#     for i in range(_):
#         angle = 360/_
#         vaishuqt.forward(100)
#         vaishuqt.right(angle)

######################################





# for _ in range(200):
#     vaishuqt.width(5)
#     vaishuqt.forward(30)
#     vaishuqt.setheading(random.choice(direction))
#     
    