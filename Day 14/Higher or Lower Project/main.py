#Display Art
import random
import art
import game_data
print(art.logo)
SCORE = 0
#generate random data from dictionary
def gen_ran():
    random_option = random.choice(game_data.data)
    return random_option



#Format the account into printable format
def format(ran_A, ran_B):
    print(f"Compare A:{ran_A['name']}, a {ran_A['description']}, from {ran_A['country']}")
    print(art.vs)
    print(f"Against B:{ran_B['name']}, a {ran_B['description']}, from {ran_B['country']}")

#Ask user for a guess
def ask_guess():
    choice = input("Who has more followers? Type 'A' or 'B': ")
    if choice == 'A':
        return "A"
    elif choice == 'B':
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

game_over = False
while game_over is not True:
    format(random_A, random_B)
    guess = ask_guess()
    if check(guess,random_A,random_B) == True:
        SCORE += 1
        print(f"You're right! Current Score:{SCORE}")
    else:
        print(f"Sorry, that's wrong.Final Score:{SCORE}")
        game_over = True