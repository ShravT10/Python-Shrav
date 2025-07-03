import random



def compare(hand1,hand2):
    if hand1==hand2:
        print("Its a draw")
        print(f"Computer's final hand is {computer_cards}")
        gameover=True
    elif hand2>hand1:
        print(f"Computer's final hand is {computer_cards}")
        print("You Lose , Comp's score was close to 21")
        gameover=True
    elif hand2<hand1:
        if hand2<17:
            computer_cards.append(random.choice(cards))
            comp_score=calc_score(computer_cards)
            print("The Comp's score was less than 17, hence it drew a card")
            if comp_score>21:
                print("Comp's score is greater than 21 , You win")
                print(f"Computer's final hand is {computer_cards}")
                gameover=True
                return
            
            compare(player_score,comp_score)
        else:
            print(f"Computer's final hand is {computer_cards}")
            print("You won ! Your score was Closer to 21")
            gameover=True
                
def calc_score(card):
        if sum(card)==21 and len(card)==2:
          return 0
        
        if 11 in card and sum(card)>21:
            cards.remove(11)
            cards.append(1)
        return sum(card)

def score_checker():
        if player_score==0:
            print(f"Your Hand is {player_cards} your score : {player_score}")
            print("You have a BlackJack you Won")
            return True
        elif comp_score==0:
            print(f"Computer's final hand is {computer_cards} Comp's score:{comp_score}")
            print("The dealer had a BlackJack you Lost")
            return True
        elif player_score>21:
            print("Game over your sum is over 21")
            print(f"Computer's final hand is {computer_cards} Comp's score:{comp_score}")
            gameover=True
            temp=True
            return
        elif comp_score>21:
            print(f"Computer's final hand is {computer_cards} Comp's score:{comp_score}")
            print("Game over the comp sum is ,over 21")
            gameover=True
            temp=True
            return
        else:
            print(f"Your Hand is {player_cards} your score : {player_score}")
            return False
            

def draw_checker():
    if player_score>21:
            print("Game over your sum is over 21")
            print(f"Computer's final hand is {computer_cards} Comp's score:{comp_score}")
    else:
        print(f"Your Hand is {player_cards} your score : {player_score}")
        temp = False


gameover = False
 
while gameover==False:
    char = input("Do you wanna play a game of black jack? y/n : ")
    if char == 'y' or char == 'Y':
        cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
        player_cards=[]
        computer_cards=[]
        for x in range(2):
            player_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))
                    
        player_score=calc_score(player_cards)
        comp_score=calc_score(computer_cards)
        #score_checker()
        print(f"Computer's First card is {computer_cards[0]}")  
        # temp=False 
    
        temp=score_checker()
        
        while temp == False:
            draw=input("Do you wanna draw a card? y/n")
            if draw=='y' or draw=='Y':
                player_cards.append(random.choice(cards))
                player_score=calc_score(player_cards)
                draw_checker()
                temp=False
            else:
                temp=True
                print("\n")
                compare(player_score,comp_score)
                print("\n")

        new=input("Do you wanna play one more time? y/n")
        if new=='y' or new=='Y':
            gameover=False
        else:
            gameover=True


        
    

         
