from random import randint
from sys import exit

while True:
    number = randint(1,10)
    print("What number between 1 and 10 am I thinking?")
    c=1

    while True:
        guess = input("Try to guess\n")

        if guess == "exit":
            exit()
        elif int(guess) == number:
          print(f"You nailed it and it took you only {c} tries.")
          break
        elif int(guess) < number:
         print("Too low.")
         c+=1
        elif int(guess) > number:
         print("Too high.")
         c+=1
