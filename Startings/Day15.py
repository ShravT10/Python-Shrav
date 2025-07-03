MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money_gained=0

def money(price,choice):
    '''Calculates Change and Takes input of Money'''
    quarter=int(input("How many quarter? : "))
    dime=int(input("How many dimes? : "))
    nickel=int(input("How many nickels? : "))
    penny=int(input("How many pennies? : "))
    
    total=(quarter*0.25)+(dime*0.10)+(nickel*0.05)+(penny*0.01)
    if total>price:
        print(f"Here is your change : {round(total-price,2)}$")
        print(f"Here is your {choice} enjoy!")
    else:
        print("Sorry that's not enough money. Refunds given")
        return

def making_coffee(choice,a,b,c):
    global money_gained
    if choice=="espresso":
        if a and b and c > 0:
            money(1.50,"espresso")
            money_gained+=1.50
        else:
            print("OH NO you ran out of resources !")
            return
            
    elif choice=="latte":
        if a and b and c > 0:
            money(2.50,"latte")
            money_gained+=2.50
        else:
            print("OH NO you ran out of resources !")
            return
            
    elif choice=="cappucino":
        if a and b and c > 0:
            money(3,"cappucino")
            money_gained+=3
        else:
            print("OH NO you ran out of resources !")
            return
            
    elif choice=="report":
        print(f'Water : {resources["water"]} ml')
        print(f'Milk : {resources["milk"]} ml')
        print(f'Coffee : {resources["coffee"]} g')
        print(f'Money : {money_gained}$')

    elif choice=="off":
        print("TING TING machine turned off !")
          

machine = False

while machine!=True:
    order = input("What would you like ? (espresso/latte/cappucino)")
    if order == "espresso":
        resources["water"]=resources["water"]-50
        resources["coffee"]=resources["coffee"]-18
        making_coffee("espresso",resources["water"],resources["coffee"],resources["milk"])
        

    elif order == "latte":
        resources["water"]=resources["water"]-200
        resources["coffee"]=resources["coffee"]-24
        resources["milk"]=resources["milk"]-150
        making_coffee("latte",int(resources["water"]),int(resources["coffee"]),int(resources["milk"]))
        
    
    elif order == "cappucino":
        resources["water"]=resources["water"]-250
        resources["coffee"]=resources["coffee"]-24
        resources["milk"]=resources["milk"]-100
        making_coffee("cappucino",resources["water"],resources["coffee"],resources["milk"])
        

    elif order == "report":
        making_coffee("report",1,2,3)
    
    elif order == "off":
        making_coffee("off",1,2,3)
        machine = True


    


