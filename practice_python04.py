i = int(input())
x = list(range(1,i+1))
d = []
for e in x:
    if i%e == 0:
        d.append(e)
print(d)
