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
def transaction_succesful(money_recieved,drink_cost):
    if money_recieved < drink_cost:
        print(f"Sorry that is not enough money to buy. Money Refunded.")
        return False
    change = round(money_recieved - drink_cost,2)

    if change > 0:
        print(f"Here is your ${change} in change.")
    return True

def report():
    print(f"Water: {resources['water']},\nMilk: {resources['milk']},\nCoffee: {resources['coffee']},\nMoney: {money}")

def insert_coin():
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total = (.25 * quarters) + (.10 * dimes) + (.05 * nickels) + (.01 * pennies)
    return round(total,2)

def make_coffee(drink_name,ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}☕ Enjoy!")

def check_resources(ingredient):
    for item in ingredient:
        if ingredient[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False

    return True


machine_on = True
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        report()
    else:
        drink = MENU[choice]
        ingredients = drink["ingredients"]
        cost = drink["cost"]

        if check_resources(ingredients):
            payment = insert_coin()

            if transaction_succesful(payment,cost):
                money += cost
                make_coffee(choice,ingredients)

