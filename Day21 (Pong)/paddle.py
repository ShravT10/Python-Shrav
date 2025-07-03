from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.locs = [(350,0),(-350,0)]
        self.pads = []
        for _ in self.locs:
            paddle = Turtle()
            paddle.shape("square")
            paddle.color("white")
            paddle.shapesize(stretch_len=1,stretch_wid=5)
            paddle.up()
            paddle.goto(_)
            self.pads.append(paddle)
    
    def up(self):
        self.new_y = self.pads[0].ycor()+25
        self.pads[0].goto(self.pads[0].xcor(),self.new_y)
    
    def down(self):
        self.new_y = self.pads[0].ycor()-25
        self.pads[0].goto(self.pads[0].xcor(),self.new_y)
    
    def up1(self):
        self.new_y = self.pads[1].ycor()+25
        self.pads[1].goto(self.pads[1].xcor(),self.new_y)
    
    def down1(self):
        self.new_y = self.pads[1].ycor()-25
        self.pads[1].goto(self.pads[1].xcor(),self.new_y)