############ NUMBER QUESSER GAME ############

import random 

Numbers=[]
for _ in range(1,101):
    Numbers.append(_)

chosen_no = random.choice(Numbers)

def guesser(attempts,chosen_no):
    '''main function which checks quesses and chosen number'''
    print(f"\nYou have {attempts} attempts ")
    gameover = False
    while gameover==False:
        quess=int(input("Quess a number : "))
        if attempts-1>0:
            if quess>chosen_no:
                print("\nToo High")
                attempts-=1
                print(f"You have {attempts} attempts left !")
            
            elif quess<chosen_no:
                print("\nToo low")
                attempts-=1
                print(f"You have {attempts} attempts left !")
                
            
            else:
                print(f"WOOHOO ! You quessed the number")
                print(f"and you have 0 attempts left !")
                gameover=True
                return
        else:
            print(f"I am sorry you have {attempts} left :(")
            print(f"The number was {chosen_no}")
            gameover=True
            return
            

print("WELCOME TO NUMBER GUESSING GAME !")
diff=input("What difficulty you want to play on , 'hard' or 'easy'?")
if diff == 'hard' or diff == 'HARD':
    attempts = 5
    guesser(attempts,chosen_no)

else:
    attempts = 10 
    guesser(attempts,chosen_no)