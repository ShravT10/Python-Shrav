from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l = 0 
        self.r = 0

    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l , align="center",font=("courier",80,"normal"))
        self.goto(100,200)
        self.write(self.r , align="center",font=("courier",80,"normal"))

    def inc_r(self):
        self.r += 1
        self.update()
    
    def inc_l(self):
        self.l += 1
        self.update()