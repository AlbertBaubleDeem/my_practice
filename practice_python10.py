from random import sample

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

same = set([elem for elem in a for elem2 in b if elem == elem2])
print("Same " , same) 


x = [1, 2, 3]
y = [5, 10, 15]
customlist = [a*b for a in x for b in y if a*b%2 != 0]
print("Customlist " , customlist) 


a = sample(range(100), 20)
b = sample(range(100), 40)

random = set([elem for elem in a if elem in b])
print("Random " , random) 

#Solution from the page
a = sample(range(1,30), 12)
b = sample(range(1,30), 16)
result_overlaps = [i for i in set(a) if i in b]
result = [i for i in result_overlaps if result_overlaps.count(i) == 1]