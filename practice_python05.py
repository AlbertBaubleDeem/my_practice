a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for e in a:
    for e2 in b: #doesn't need this second loop
        if e == e2:
            c.append(e)
print(c)

c = []
for e in a:
    if e in b:
        c.append(e)
print(c)

c = [elem for elem in a if elem in b] #one liner :-)
print(c)

from random import randint

a = [randint(0,50) for e in range(10)]
b = [randint(0,50) for e in range(10)]
c = []
for e in a:
    if e in b: #works the same.
        c.append(e)
print(a)
print(b)
print(c)