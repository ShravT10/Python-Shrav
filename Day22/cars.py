from turtle import Turtle 
import random
COLORS = ["red" , "blue" , "green" , "yellow" , "purple" , "orange" , "brown" , "indigo" , "pink"]
posi = [260,240,220,200,180,160,140,120,100,80,60,40,20]
class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.carrs = []
        for _ in posi:
            a = random.choice(COLORS)
            self.shape("square")
            self.shapesize(stretch_len=2,stretch_wid=1)
            self.penup()
            self.color(a)
            self.goto(280,_)
            self.carrs.append()