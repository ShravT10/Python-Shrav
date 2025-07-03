from Food import food

class score(food):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.goto(0,270)
        self.write(f"SCORE : {self.score}",align="center",font=("Arial",15,"normal"))
        self.hideturtle()

    def inc(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE : {self.score}",align="center",font=("Arial",15,"normal"))

    def out(self):
        self.home()
        self.write(f"GAME OVER",align="center",font=("Arial",15,"normal"))