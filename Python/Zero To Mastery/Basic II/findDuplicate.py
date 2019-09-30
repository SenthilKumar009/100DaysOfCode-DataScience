myList = ['a', 'b', 'c', 'd', 'b', 'e', 'c', 'f']
myDict = {}

#Solution 1
for char in myList:
    if (char in myDict):
        myDict[char] += 1
    else:
        myDict[char] = 1

for key, value in myDict.items():
    if value > 1:
        print(key, end='\n')
    #print("%s : %d" %(key, value))

#Solution 2:

duplicates = []

for value in myList:
    if myList.count(value)>1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates) 