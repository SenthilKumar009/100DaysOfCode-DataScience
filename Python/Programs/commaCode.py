spam = ['apples', 'bananas', 'tofu', 'cats']

joinString =''

for i in range(len(spam)):
    if i == len(spam)-1:
        joinString += 'and ' + spam[i]
    else:
        joinString += spam[i]+', '

print(joinString)