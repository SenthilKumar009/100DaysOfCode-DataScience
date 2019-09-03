testString = '''Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars'''

stringList = list(testString.split('\n'))
print(len(stringList))

for i in range(len(stringList)):
    stringList[i] = '* ' + stringList[i]

for text in stringList:
    print(text)