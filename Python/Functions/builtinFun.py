''' All function '''
myList = [True, True, 1, 2]

if all(myList):
    print('All the values are True')
else:
    print('Few of the values are False')

''' All function '''
myList = [True, True, 1, 0]

if any(myList):
    print('Few of the values are True')
else:
    print('All the values are False')
