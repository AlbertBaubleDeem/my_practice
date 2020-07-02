# while True:
#     def get_integer(text="Give me any whole number: "):
#         return int(input(text))
#     def prime():
#         x = list(range(2,n))
#         for i in x:
#             if n%i == 0:
#              return False
#             else:
#              return True

#     def answer(question):
#         if question == True:
#             print(str(n) + " is a prime.")
#         if question == False:
#             print(str(n) + " is NOT a prime.")

#     n = get_integer()
#     answer(prime())


def get_integer(text="Give me any whole number: "):
    user_input = input(text)
    try:
        if float(user_input).is_integer():
            print("Yes")
            return int(float(user_input))
        else:
            return False
    except ValueError:
        return False
def prime():
    if n > 1:
        x = [i for i in range(2,abs(n)) if n%i == 0]
        return x
    else:
        return [1]
def answer(question):
    if not question:
        print(str(n) + " is a prime.")
    else:
        print(str(n) + " is NOT a prime.")

while True:
    n = get_integer()
    print(n)
    if n:
        answer(prime())
        print(prime())
    else:
        print("This is not a valid number. Please try again.")