import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

#Extracted Data
main_data = pandas.read_csv("50_states.csv")
state = main_data.state.tolist()

correct_ans = []
to_learn = []
game_on = True

while game_on:
    answer = screen.textinput(title=f"Guessed: {len(correct_ans)}/50" , prompt="What is your Guess?").title()

    if answer == 'Stop':
         break
    if answer in state:
            if answer not in correct_ans:
                shrav = turtle.Turtle()
                shrav.penup()
                shrav.hideturtle()
                cord = main_data[main_data.state == answer]
                shrav.goto(cord.x.item(),cord.y.item())
                style = ('Courier', 7 , 'italic')
                shrav.write(answer, font=style)
                correct_ans.append(answer)
            
            if len(correct_ans) == 50:
                end = turtle.Turtle()
                end.penup()
                end.hideturtle()
                end.goto(0,0)
                style = ('Courier', 20 )
                end.write("YOU WON !",font=style)
                game_on = False

for i in state:
     if i not in correct_ans:
          to_learn.append(i)
          
learn = pandas.DataFrame(to_learn)
learn.to_csv("Missed_States.csv")


turtle.mainloop()