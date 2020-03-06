#spam = ['apples', 'bananas', 'tofu', 'cats']
spam = ['apples', 'bananas']

joinString =''

for i in range(len(spam)):
    if len(spam) == 1:
        joinString += spam[0]
    elif i == len(spam)-1:
        joinString += 'and ' + spam[i]
    else:
        joinString += spam[i]+', '

print(joinString)