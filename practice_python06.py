# word = str(input())
# lng = len(word)/2
# def symmetry():
   
#    if len(word)%2 == 0:
#        if word[0:lng+1] == word[:lng:-1]:
#            return True
#        else:
#            return False
#    else:
#      return False

# print(symmetry())

word = str(input())
def palindrome():
    
    if word == word[::-1]:
        return True
    else:
       return False

print(palindrome())