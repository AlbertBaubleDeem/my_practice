def reverse_sentence(x):
    list_words = x.split(sep=' ', maxsplit=-1)
    list_reversed = list_words[::-1]
    sentence_reversed = ' '.join(list_reversed)
    return sentence_reversed

print(reverse_sentence(input()))

def reverse_string2(x):
    return ' '.join(x.split(sep=' ', maxsplit=-1)[::-1])

print(reverse_string2(input()))