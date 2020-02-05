oneFile = []
with open('test1.txt') as file:
    for line in file:
        oneFile.append(line.strip())

print(oneFile)

print(__name__)