import random
is_game_over = False 
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
def deal_card():
    '''Chooses a random card'''
    card=random.choice(cards)
    return card 
def calc_score(card):
    '''Takes a list and calculates its sum'''
    if sum(card)==21 and len(card)==2:
        return 0
    
    if 11 in card and sum(card)>21:
        cards.remove(11)
        cards.append(1)
    
    return sum(card)

my_c=[]
pc_c=[]

for i in range(2):
    my_c.append(deal_card())
    pc_c.append(deal_card())

user_score=calc_score(my_c)
comp_score=calc_score(pc_c)

print(f"Your hand is {my_c}, Your score: {user_score}")
print(f"Dealer's First card is {pc_c[0]}")

if user_score == 0 or comp_score==0 or user_score>21:
    is_game_over = True

    