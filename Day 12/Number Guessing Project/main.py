import art
print(art.logo)
import random
random_guess = random.randint(1,100)
def guess_game(game_level):
    if game_level == "easy":

        for i in range(10):
            print(f"You have {10-i} attempts remaining.")
            user_choice = int(input("Enter the number you guessed:"))
            print(game_check(user_choice))

    if game_level == "hard":

        for i in range(5):
            print(f"You have {5-i} attempts remaining.")
            user_choice = int(input("Enter the number you guessed:"))
            print(game_check(user_choice))

def game_check(check):
    if check > random_guess:
        return "Too High.\nGuess Again."
    elif random_guess > check:
        return "Too Low.\nGuess Again."
    elif check == random_guess:
        return "You got the right answer"


print("""Welcome to Number Guessing Game!\nI am thinking of a Number between 1 and 100""")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
guess_game(difficulty)