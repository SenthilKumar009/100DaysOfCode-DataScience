pair = int(input('Enter the total pair of numbers:'))

list1 = []
list2 = []
for i in range(0,pair):
    number1, number2 = input().split()
    list1.append(int(number1))
    list2.append(int(number2))

sum = []
for i in range(0,pair):
    sum.append(list1[i]+list2[i])

for i in sum:
    print(i, end=' ')

print()