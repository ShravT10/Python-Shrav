import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

timespeed = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(timespeed)
    screen.update()
    car.create_car()
    car.move_car()
    
    # for _ in car.all_cars:
    #     if _.distance(player) < 20:
    #         score.gameover()
    #         game_is_on = False

    if player.ycor()==280:
        timespeed/=3
        player.goto(0,-280)
        score.updatelevel()

screen.exitonclick()
        