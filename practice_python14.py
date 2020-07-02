a = [1, 1, 2, 3, 5, 8, 8,13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def get_uniques(a):
    c = []
    for e in a:
        if e not in c:
            c.append(e)
    return c

print(get_uniques(a))

def get_uniques_sets(a):
    c = set(a)
    return list(c)

print(get_uniques_sets(a))