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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    }
money=0
game = True



def resource_sufficient(ingredients):
    for item in drink["ingredients"]:
        if ingredients[item] >= resources[item]:
            print("There are not sufficient resources")
            return False
    return True


def proccess_coins():
    quarters=float(input("Enter the number of quarters: "))
    dimes=float(input("Enter the number of dimes"))
    Nickel=float(input("Enter the number of Nickels"))
    Pennies=float(input("Enter the number of pennies"))
    Total= (quarters*.25) + (dimes*.10) + (Nickel*.10) + (Pennies*.01)
    return Total

def check_transaction(proccesscoins,drinkprice,money):
    if Total<drinkprice:
        print("you do not have enough money")
        return False
    else:
        print("You have enough here's you drink  ")
        money+=drinkprice
        print(f"Your change is {Total-drinkprice}")
    return money

while game == True:
    choice = input("☕What would you like?(espresso/latte/cappuccino:")
    if choice == "off":
        game = False
    elif choice == "report":
      print(f"water:{resources["water"]}ml")
      print(f"milk:{resources["milk"]}ml")
      print(f"coffee:{resources["coffee"]}g")
      print(f"money:{money}$")
    else:
        drink=MENU[choice]
        print(drink)
        resource_sufficient(drink["ingredients"])
        Total = proccess_coins()
        money=check_transaction(Total,drink["cost"],money)

