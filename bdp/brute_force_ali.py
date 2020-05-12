x=0
while x < len_reference:
    if reference[x] == word[0]:
        if reference[x:x + len_word] == word:
            places.append(x)
        if find_only_first: 
            break
    x = x +1
print(places)