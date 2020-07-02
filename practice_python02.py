import sys

while True:
    n = (input("Write any whole number that comes to your mind." + "\n"))
    if n == "stop":
        sys.exit()
    elif int(n) % 2 == 0:
        print("Your number is even.")
    else:
        print("You are odd.")