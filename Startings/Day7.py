import random

gameover=False
list=["ardvark","babool","camel"]
chosen_word = random.choice(list)
print(chosen_word)
display = []
life=5

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# def debug():
#      print("******ignore******")
#      print("chosen word is : " ,chosen_word)
#      print("guessed is : " ,guess)
#      print("letter is: ", letter)
#      print("posi is: " , posi)
#      print("******ignore******")

for i in range(len(chosen_word)):
        display.append("_")

while gameover==False:
        guess = input("Guess a word : ")
        for posi in range(len(chosen_word)): 
                letter=chosen_word[posi]
                if letter==guess:
                    display.remove("_")
                    display.insert(posi,guess)
        
        

        print(' '.join(display))
        if '_' in display:
            gameover=False
        else:
            gameover=True
            print("You win")
        if guess in chosen_word:
              gameover=False
        else:
              life -=1
              if life==0:
                gameover=True
                print(stages[0])
                print("game over")
              if life==4:
                print(stages[5])
              elif life==3:
                print(stages[4])    
              elif life==2:
                 print(stages[2])
              elif life==1:
                 print(stages[1])
        
        
        
                
            

            
        
        
            

        

