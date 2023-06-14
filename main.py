from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu= Menu()

is_on=True

while is_on:
    options=menu.get_items()
    choice= input(f"What would like to have {options}: ")
    if choice=="off":
        is_on=False
        print("The Coffee Machine is closed.")
    elif choice=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink= menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)