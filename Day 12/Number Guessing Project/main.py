import art
print(art.logo)
import random
random_guess = random.randint(1,100)

def game_check(check):
    if check > random_guess:
        print("Too High.\nGuess Again.")
        return False
    elif random_guess > check:
        print("Too Low.\nGuess Again.")
        return False
    elif check == random_guess:
        print("You got the right answer")
        return True


def guess_game(game_level):
    if game_level == "easy":
        attempts = 10
    if game_level == "hard":
        attempts = 5

    for i in range(attempts):
        print(f"You have {attempts-i} attempts remaining.")
        user_choice = int(input("Enter the number you guessed:"))
        result = game_check(user_choice)
        if result:
            break
    if not result:
        print(f"Sorry you Lost, the guess was {random_guess}")




print("""Welcome to Number Guessing Game!\nI am thinking of a Number between 1 and 100""")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
guess_game(difficulty)