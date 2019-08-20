i = 0
numbers  = []

while i < 6:
    print('At the top i is {}'.format(i))
    numbers.append(i)

    i += 1
    print('Numbers:', numbers)

    print('At the bottom i is {}'.format(i))

print("The Numbers:")

for i in numbers:
    print(i)