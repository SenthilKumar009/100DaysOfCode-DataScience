sent = 'Print only the words that start with with s from the given sentance'
listStr = sent.split(' ')

print(listStr)

for val in listStr:
    if val[0] == 's' or val[0] == 'S':
        print(val)