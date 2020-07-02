print(6+7)
print(8**2)
print()

shopping=["eggs", "ham", "cheese", "butter", "condoms"]
for item in shopping:
    print(item)
prices=[9.42, 5.67, 3.25, 13.40, 7.50]
print(*prices[:4], sep="\n")
cprice = prices[4]
print(cprice*3)
print()

print(len("blood-oxygenation level dependent functional magnetic resonance imaging"))
print()

snack = "huel"
print((snack+" ")*100)

#print(dir(snack))
#help(snack.capitalize)

print(snack.center(30," "))
print(*prices[:5])