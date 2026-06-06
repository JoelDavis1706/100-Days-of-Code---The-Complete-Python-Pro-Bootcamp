import art

def add(n1, n2):
    return n1 + n2

#TODO : Write out the other 3 functions that is subtract, divide and multiply
def subtract(n1,n2):
    return n1 - n2
def divide(n1,n2):
    return n1/n2
def multiply(n1,n2):
    return n1*n2

# TODO : Add these 4 functions to dictionary as the values . Keys = "+","-","/","*"

operations = {
    "+":add,"-":subtract,"/":divide,"*":multiply
}

def calculator():
    print(art.logo)
    should_acumulate = True
    number1 = float(input("Enter the first number:"))

    while should_acumulate:
        for symbols in operations:
            print(symbols)
        user_operation = input("Enter the operation you want to use:")
        number2 = float(input("Enter the second number:"))
        result = operations[user_operation](number1,number2)
        print(f"{number1} {user_operation} {number2} = {result}")

        game_continue = input(f"Do you want to continue calculation with {result}, type y for yes, n for no and exit to exit:")
        if game_continue == "y":
            number1 = result
        elif game_continue == "n":
            should_acumulate = False
            print("\n" * 50)
            calculator()
        elif game_continue == "exit":
            break

calculator()