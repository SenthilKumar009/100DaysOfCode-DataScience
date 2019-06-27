pair = int(input('Enter the total pair of numbers:'))

list1 = []
list2 = []
for i in range(0,pair):
    number1, number2 = input().split()
    list1.append(int(number1))
    list2.append(int(number2))

min = []
for i in range(0,pair):
    if list1[i] > list2[i]:
        min.append(list2[i])
    else:
        min.append(list1[i])

for val in min:
    print(val, end=' ')

print()