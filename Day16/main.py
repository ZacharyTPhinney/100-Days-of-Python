from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



money_machine=MoneyMachine()
coffee_Maker=CoffeeMaker()
menu=Menu()
is_on=True
while is_on:
  options = menu.get_items()
  choice=input(f"What would you like {options}?\n")
  if choice=="off":
    if_on=False
  elif choice=="report":
    coffee_Maker.report()
    money_machine.report()
  else:
    
    drink=menu.find_drink(choice)
    suf = coffee_Maker.is_resource_sufficient(drink)
    pay = money_machine.make_payment(drink.cost)
    coffee = coffee_Maker.make_coffee(drink)
    