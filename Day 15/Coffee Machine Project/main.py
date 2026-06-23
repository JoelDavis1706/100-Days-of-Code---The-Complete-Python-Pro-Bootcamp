from random import choice

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



money = 0
def ask_user():
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    return choice

def report():
    return f"Water: {resources['water']}, Milk: {resources['milk']}, Coffee: {resources['coffee']}"

def insert_coin():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    dollars = (.25 * quarters) + (.10 * dimes) + (.05 * nickels) + (.01 * pennies)
    return dollars


machine_off = False
print(report())
print(f"Money: {money}")
choice = ask_user()
if choice == "report":
    print(report())
elif choice == "off":
    machine_off = True
else:
    print("Please insert coins:")
    total = round(insert_coin(),2)
    print(f"Inserted Money: {total}")
    cost = MENU[choice]["cost"]
    if cost < total:
        change = total - cost
        print(f"Change: {change}")
        print(f"Here is your {choice}☕ Enjoy!")
    else:
        print(f"You don't have enough cash to buy {choice}.")
