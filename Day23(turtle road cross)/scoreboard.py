from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-270,260)
        self.updatelevel()

    def updatelevel(self):
        self.clear()
        self.write(f"Level : {self.level}" , align="left",font=FONT)
    
    def increaselevel(self):
        self.level+=1
        self.updatelevel()

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER")

