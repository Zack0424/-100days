from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

while True:
    x = input(f"What would you like? ({menu.get_items()}): ")
    if x == "report":
        coffeeMaker.report()
        moneyMachine.report()
    elif x == "off":
        break
    elif x in menu.get_items():
        if coffeeMaker.is_resource_sufficient(menu.find_drink(x)):
            if moneyMachine.make_payment(menu.find_drink(x).cost):
                coffeeMaker.make_coffee(menu.find_drink(x))
