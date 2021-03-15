def orderable(coffee):
    for i in MENU[coffee]["ingredients"]:
        if resources[i] < MENU[coffee]["ingredients"][i]:
            print(f"Sorry there is not enough {i}.")
            return False
        return True
def order(coffee):
    for i in MENU[coffee]["ingredients"]:
        resources[i] -= MENU[coffee]["ingredients"][i]
    resources["money"] += MENU[coffee]["cost"]
    print("Here is your latte. Enjoy!")
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
    "money": 0
}

#TODO: 1.Loop
while True:
    x = input("What would you like? (espresso/latte/cappuccino): ")
    if x == "report":
        print(f"""water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${resources["money"]}""")
    elif x == "off":
        break
    elif x in MENU.keys():
        if orderable(x) == True:
            q = int(input("Quarters: "))*0.25
            d = int(input("Dimes: "))*0.1
            n = int(input("Nickels: "))*0.05
            p = int(input("Pennies: "))*0.01
            money = q+d+n+p
            if money < MENU[x]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            elif money == MENU[x]["cost"]:
                order(x)
            else:
                print(f"Here is ${money-MENU[x]['cost']:.2f} dollars in change")
                order(x)