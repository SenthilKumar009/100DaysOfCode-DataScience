xFile = open('test.txt')
#for x in xFile:
#    print(x)

count = 0
for line in xFile:
    count = count + 1

print('Total Line:', count)

fHand = open('test.txt')
#inp = fHand.read()
#print('Total Char in the File:', len(inp))
#print(inp[:24])

for line in fHand:
    line = line.rstrip()
    if line.startswith('Ref'):
        print(line)
