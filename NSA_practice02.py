snack = "huel"
print(snack*100)
Nsnack = "pussy"
print((Nsnack+" "+snack+" ")*100)
shopping=["eggs", "ham", "cheese", "butter", "condoms"]
prices=[9.42, 5.67, 3.25, 13.40, 7.50]
groceries = shopping
print(snack in groceries)
print(Nsnack in groceries)
#print(dir(snack))
snack, Nsnack = Nsnack, snack
print(snack, Nsnack)
import random
from random import randint
#help(random.randint)
print((snack+" ")*randint(1,100))
#print(dir(random))
print(random.choice(groceries))
#print(int(random.choice(prices)))
Wprice = random.choice(prices)
print("The price is:", Wprice)
if Wprice <=10:
    print("Your change isv:", 10-Wprice)
else:
    print("You win:", abs(10-Wprice))