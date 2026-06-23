#Display Art
import random
import art
import game_data

#generate random data from dictionary
def gen_ran():
    random_option = random.choice(game_data.data)
    return random_option



#Format the account into printable format
def display_accounts(ran_A, ran_B):
    print(f"Compare A:{ran_A['name']}, a {ran_A['description']}, from {ran_A['country']}")
    print(art.vs)
    print(f"Against B:{ran_B['name']}, a {ran_B['description']}, from {ran_B['country']}")

#Ask user for a guess
def ask_guess():
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if choice == 'a':
        return "A"
    elif choice == 'b':
        return "B"

#Check if user is correct
def check(guess,ran_A,ran_B):
    greater = ""
    if ran_A['follower_count'] > ran_B['follower_count']:
        greater = "A"
    elif ran_B['follower_count'] > ran_A['follower_count']:
        greater = "B"
    if guess == greater:
        return True
    else:
        return False
## - Check follower count of each account
## - Use if statement to check if user is correct


#Give user feedback on their guess

#Keeping the score

#make the game repeatable.

#make the account at position at B become the next A

random_A = gen_ran()
random_B = gen_ran()
if random_A == random_B:
    random_A = gen_ran()
game_over = False
while not game_over:
    score = 0
    print(art.logo)
    display_accounts(random_A, random_B)
    guess = ask_guess()
    if check(guess,random_A,random_B):
        score += 1
        random_A = random_B
        random_B = gen_ran()
        print("\n" * 30)
        print(f"You're right! Current Score:{score}")

    else:
        print(f"Sorry, that's wrong.Final Score:{score}")
        game_over = True