def find_word(strng, word):
    flag = False
    for x in word:
        if x in strng:
            flag = True
        else:
            flag = False
            break

    return flag

print(find_word('Nabucodonosor','donor'))
print(find_word('Nabucodonosor','donot'))