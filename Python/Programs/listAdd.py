catNames = []

while True:
    print('Enter the name of the cat ' + str(len(catNames)+1) + ' Or enter nothing to stop!!!')

    name = input('> ')
    if name == '':
        break
    catNames = catNames + [name]

print('The cats are', catNames)

name = input('Enter the cat name to uppend: ')
catNames.append(name)

name = input('Enter the cat name to insert: ')
catNames.insert(2, name)

print('the cats are:', end=' ')
for cat in catNames:
    print(cat, end=' ')

print()