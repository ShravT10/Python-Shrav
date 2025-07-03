from turtle import Turtle , Screen
import random
myscreen = Screen()
myscreen.setup(width=500,height=400)
user_ans=myscreen.textinput(title="Make a bid",prompt="Satta laga chal bkp")

game = True

color = [ 'red','orange','blue','yellow','green']
pos = -100
listo=[]
for _ in color:
    tim = Turtle(shape="turtle")
    tim.up()
    tim.color(_)
    tim.goto(x=-230,y=pos)
    pos += 35
    listo.append(tim)

while game:
    for turtle in listo:
        turtle.forward(random.randint(0,10))
        if turtle.xcor()>230:
            if turtle.color()==user_ans:
                print("You won!")
                game=False
            else:
                print("Ah! you lost (katgaya)")
                game=False


myscreen.exitonclick()