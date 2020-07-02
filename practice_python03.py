print("0th part: ")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for a in range(0,5):
   print(a)

print("1st part: ") 
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
y = []
for e in a:
    if e < 5:
        y.append(e)
print(y)

print("2nd part: ")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
y = []

input = int(input())
for e in a: 
    if input > e:
        y.append(e)

print(y)

print("3nd part: ")
print([number for number in a if number < 5])