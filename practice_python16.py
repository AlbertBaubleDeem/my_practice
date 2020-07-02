import string
import secrets
import random
import timeit

def generate_strong_pass():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(8))
    return password
def generate_weak_pass():
    start = timeit.default_timer()
    weak_password_tuple= tuple(open('Wordlist_82_million.txt' , 'r' , newline=''))
    stop = timeit.default_timer()
    global execution_time 
    execution_time = stop - start
    password_string = random.choice(weak_password_tuple)
    password = password_string.rstrip('\n')
    return password

while True:
    i = input("To generate a password, press ENTER. To exit, type 'exit'.\n")
    if i == "":
        j = input("For a weak password, type 'weak.' For a strong password, type 'strong'.\n")
        if j == "strong":
            
            print("Your new password is:\n"+  generate_strong_pass() + "\n")
        elif j == "weak":
            
            print("Your new password is:\n"+ generate_weak_pass())
            print("It took this long to calculate:", execution_time, "\n")
            
    elif i == "exit":
        exit()
    else:
        print("This is not a valid input, please try again.")