from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        chance = random.randint(1,6)
        if chance == 1 or chance == 6:
            car = Turtle("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2,stretch_wid=1)
            car.penup()
            y = random.randint(-260,280)
            car.goto(300,y)
            self.all_cars.append(car)
        
    def move_car(self):
        for car in self.all_cars:
            car.backward(MOVE_INCREMENT)
