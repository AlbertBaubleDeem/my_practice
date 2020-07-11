'''
This is a game of Cows And Bulls

Game uses gen_num method to randomly generate a 4-digit number *secret_num*. 
User uses input function to enter their guess *guess* on the generated 4-digit number. 

For every digit that the user guessed correctly in the correct place, they have a “cow." The correct digit is stored in *cows* list.
For every digit the user guessed correctly in the wrong place is a “bull.” The correct digit is stored in *bulls* list.
Every time the user makes a guess, game tells user how many “cows” and “bulls” they have by printing len(bulls) and len(cows).

Once the user guesses the correct number, the game is over. 

Keep track of the number of guesses the user makes throughout the game and tell the user at the end.
'''

import random

# Generates the 4 digit secret_num.
def secret_num():
    secret_num = str(random.randint(1000, 9999))
    return list(secret_num)
# Compares user's guess to the secret_num.
def compare_bulls_cows():
    for j in range(0,4):
        if guess[j] == secret_num[j]:
            cows.append(guess[j])
        elif guess[j] in secret_num:
            bulls.append(guess[j])
# Sanitizes user's input.
def playerinput(x):
    while True:
        playerinput = input(x)
        if playerinput.isdecimal and len(list(str(playerinput))) == 4:
            return playerinput 
        else:
            print("Invalid input. Please enter a 4 digit number.")

print('Welcome to the Cows and Bulls Game!')

secret_num = tuple(secret_num())
guess = tuple()
bulls =[]
cows = []
turns = 0

while True:
    turns = turns + 1
    if guess == secret_num:        
        print(f"You have won. It took you {str(turns)} turns.")
        break
    else:
        bulls =[]
        cows = []
        guess = tuple(playerinput('Enter your guess: '))
        compare_bulls_cows()

        print(f"This is your {turns}. turn. Your results are below.")
        print(f"Number of bulls: {len(bulls)}")
        print(f"Number of cows: {len(cows)}")