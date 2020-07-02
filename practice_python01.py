import datetime
import sys
while True:
    age = input("How old are you, good chap?" + "\n")
    if age == "stop":
        sys.exit()
    elif int(age) >= 100:
        print("Sod off grandpa.")
    else:
        now = datetime.datetime.now()
        diff = 100-int(age)
        print("You will turn 100 in " + str(now.year + diff) + ".")
    