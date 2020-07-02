def get_integer(text="Give me any whole number: "):
    user_input = input(text)
    try:
        if float(user_input).is_integer() and float(user_input) >= 0:
            return int(float(user_input))
        else:
            print("This is not a valid number. Please try again.")
            return False
    except ValueError:
        print("This is not a valid number. Please try again.")
        return False

def gen_fib(n):
    a = list(range(1,n-1))
    i = 1
    #print(a)
    if n==0:
        fib = []
    elif n == 1:
        fib = [1]
    elif n == 2:
        fib = [1,1]
    elif n > 2:
        fib = [1,1]
        for e in a:
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib

n = get_integer("How many Fibonacci numbers do you want to see?" + "\n")
print(gen_fib(n))

#elegant from the discussion

def fibonacci_generator(n):
    i = 1
    nth = 1
    previous_value = 0
    store = 0
    fib = []
    while i <= n:
        fib.append(nth)
        store = previous_value
        previous_value = nth
        nth = store + nth
        i += 1
    return fib

n = get_integer("How many Fibonacci numbers do you want to see?" + "\n")
print(fibonacci_generator(n))

#the best from collaboration with Lukas. Has no counter + alignes the best with the algorithm

def f(n):
    if n == 0:
        fib = []
    elif n == 1:
        fib = [1] 
    elif n == 2:
        fib = [1, 1]
    elif n > 2:
        fib = [1, 1]
        while len(fib) < n:
            fib.append(fib[-2]+fib[-1])
    return fib

n = get_integer("How many Fibonacci numbers do you want to see?" + "\n")
print(f(n))