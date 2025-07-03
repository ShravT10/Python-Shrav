import time 
from turtle import Screen
from turtke import Turtle1
from cars import Car

screen = Screen()
screen.setup(600,600)
screen.tracer(0)

me = Turtle1()
gaadi = Car()
game = True

while game:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkey(key="Up",fun=me.move)
    






screen.exitonclick()