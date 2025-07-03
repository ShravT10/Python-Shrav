from turtle import Turtle 

posi = [(0,0),(-20,0),(-40,0)]
move = 10

class Snake:

    def __init__(self):
        self.listo = []
        self.create_snake()
        self.head = self.listo[0]
        self.temp = []
    def create_snake(self):
        for _ in posi:
            self.add(_)
            
    
    def add(self,posi1):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.up()
        turtle.goto(posi1)
        self.listo.append(turtle)

    def extent(self):
        self.add(self.listo[-1].position())
    
    def move(self):
        for _ in range(len(self.listo)-1,0,-1):
            new_x = self.listo[_-1].xcor()
            new_y = self.listo[_-1].ycor()
            self.listo[_].goto(new_x,new_y)

        self.listo[0].forward(move)

    def up(self):
        if self.head.heading() != 270:
            self.listo[0].setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.listo[0].setheading(270)
    
    def right(self):
        if self.head.heading() != 0:
            self.listo[0].setheading(180)
    
    def left(self):
        if self.head.heading() != 180:
            self.listo[0].setheading(0)


    
    