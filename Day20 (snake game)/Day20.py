from turtle import Screen
import time
from snake import Snake
from Food import food
from Score import score
myscreen = Screen()
myscreen.setup(width=600,height=600)
myscreen.bgcolor("Black")
myscreen.title("Welcom to NOKIA 3310")
myscreen.tracer(0)

snakeu = Snake()
khau = food()
my_score = score()
game = True

while game:
    myscreen.update()
    time.sleep(0.1)
    snakeu.move()
    if snakeu.head.distance(khau) < 15:
        khau.ref()
        my_score.inc()
        snakeu.extent()
    
    if snakeu.head.xcor() > 280 or snakeu.head.xcor() < -280 or snakeu.head.ycor() > 280 or snakeu.head.ycor() < -280:
        my_score.out()
        game = False
    for segment in snakeu.listo[1:]:
        if snakeu.head.distance(segment) < 5:
            game = False
            my_score.out()    
            
        
    myscreen.listen()
    myscreen.onkey(key="Down",fun=snakeu.down)
    myscreen.onkey(key="Up",fun=snakeu.up)
    myscreen.onkey(key="Left",fun=snakeu.right)
    myscreen.onkey(key="Right",fun=snakeu.left)



myscreen.exitonclick()
