try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have entered a unreadable input enter in number format like 15.")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
