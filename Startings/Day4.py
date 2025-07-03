import random

# dice=random.randint(1,6)
# dice2=random.randint(1,6)
# if dice==dice2:
#     print(f"You rolled a dice and you got a {dice} and a {dice2}, a double! , you get another roll!")
#     print(f"You rolled a total of {dice+dice2}!")
# else:
#     print(f"You rolled a dice and you got a {dice} and a {dice2} !")
#     print(f"You rolled a total of {dice+dice2}!")
    
# a=random.random()*5
# b=round(a,2)
# print(a) 
# c=3.234546475
# print(round(c,2))

# number=["Universe","World","India","Maharashtra","Pune","Ravi_darshan","Parijit colony"]
# b=random.randint(0,6)

# print(f"Vaish will be the leader of {number[b]}")
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissor=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

print("Choose a number 0 for rock, 1 for paper , 2 for scissor")
a=int(input())

if a==0:
    choice=rock
    print("You choosed: Rock")
    print(rock)
elif a==1:
    choice=paper
    print("You choosed: Paper")
    print(paper)
else:
    choice=scissor
    print("You choosed: Scissor")
    print(scissor)

b=random.randint(0,2)
if b==0:
    choice1=rock
    print("Computer choosed: Rock")
    print(rock)
elif b==1:
    choice1=paper
    print("Computer choosed: Paper")
    print(paper)
else:
    choice1=scissor
    print("Computer choosed: Scissor")
    print(scissor)

if choice==choice1:
    print("Its a draw")
elif choice==rock and choice1==paper:
    print("You lose!")
elif choice==rock and choice==scissor:
    print("You win!")
elif choice==paper and choice1==scissor:
    print("You lose!")
elif choice==paper and choice1==rock:
    print("You win!")
elif choice==scissor and choice1==rock:
    print("You lose!")
else:
    print("You win!")