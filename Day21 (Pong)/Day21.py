from turtle import Turtle , Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Score

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

pedle = Paddle()
bell = Ball()
scere = Score()


r_paddle = pedle.pads[0]
l_paddle = pedle.pads[1]
screen.listen()
screen.onkey(key='Up',fun=pedle.up)
screen.onkey(key='Down',fun=pedle.down)
screen.onkey(key='w',fun=pedle.up1)
screen.onkey(key='s',fun=pedle.down1)
game = True

while game:
    time.sleep(bell.m_speed)
    screen.update()
    bell.move()
    scere.update()
    if bell.ycor() > 280 or bell.ycor() < -280:
        bell.bouncey()
    if bell.distance(r_paddle) < 50 and bell.xcor() > 320 or bell.distance(l_paddle) < 50 and bell.xcor() < -320:
        bell.bouncex()
    if bell.xcor() > 380:
        scere.inc_l()
        bell.home()
        bell.speed = 0.1 
        bell.bouncex()
    if bell.xcor() < -380:
        scere.inc_r()
        bell.home()
        bell.m_speed = 0.1
        bell.bouncex()    


screen.exitonclick() 