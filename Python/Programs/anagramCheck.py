def anagram_check(string1, string2):
    if sorted(string1.lower()) == sorted(string2.lower()):
        return 'Its an Anagram'
    else:
        return 'Its not an Anagram'

print(anagram_check('Silent', 'Listen'))
print(anagram_check('Iam', 'You'))
