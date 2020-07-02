##Works well, but too complicated
#  def first_last(a):
#     b = a
#     del b[1:-1]
#     print(b)

# first_last([5, 10, 15, 20, 25])

#Simpler solution
def first_last(a):
    return [a[0], a[-1]]

print(first_last([5, 10, 15, 20, 25]))