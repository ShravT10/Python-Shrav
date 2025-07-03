from turtle import Turtle

import random


class food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.up()
        self.shape("circle")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.ref()

    def ref(self):
        rx = random.randint(-250,250)
        ry = random.randint(-250,250)
        self.goto(rx,ry)