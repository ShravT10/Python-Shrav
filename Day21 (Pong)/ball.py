from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.up()
        self.x_new = 10
        self.y_new = 10
        self.m_speed = 0.1

    def move(self):
        self.new_x = self.xcor() + self.x_new
        self.new_y = self.ycor() + self.y_new
        self.goto(self.new_x,self.new_y)

    def bouncey(self):
        self.y_new *= -1
        self.m_speed *= 0.9
    def bouncex(self):
        self.x_new *= -1