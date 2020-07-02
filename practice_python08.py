import sys

def playerinput(x):
    while True:
        choice = input(str(x) + ", please enter your choice:\n")
        options = ("rock","paper","scissors")
        if "exit" in (choice):
            sys.exit()
        elif choice not in options:
         print("You didn't enter any of the options or made a typo. Try again.")
        else:
            return choice

print("This is a game of rock, paper, scissors.\n\
You need two players to play.")

while True:
    winner = {
    "rock, scissors" : "Player 1 wins!",
    "rock, paper": "Player 2 wins!",
    "paper, scissors": "Player 2 wins!",
    "paper, rock": "Player 1 wins!",
    "scissors, rock": "Player 2 wins!",
    "scissors, paper": "Player 1 wins!"
    }

    p1 = playerinput("Player 1")
    p2 = playerinput("Player 2")
    print(winner[f"{p1}, {p2}"])

# while True:
#     p1 = playerinput("Player 1")
#     p2 = playerinput("Player 2")
#     if p1 == p2:
#         print("It's a tie! Play again.")
#     elif p1 == "rock":
#         if p2 == "scissors":
#             print("Player 1 wins!")
#         elif p2 == "paper":
#             print("Player 2 wins!")
#     elif p1 == "paper":
#         if p2 == "scissors":
#             print("Player 2 wins!")
#         elif p2 == "rock":
#             print("Player 1 wins!")
#     elif p1 == "scissors":
#         if p2 == "paper":
#             print("Player 1 wins!")
#         elif p2== "rock":
#             print("Player 2 wins!")
