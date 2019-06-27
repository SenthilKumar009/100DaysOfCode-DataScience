total_num = int(input('Enter the total input:'))

myNum = []

for i in range(0,total_num):
    num = int(input('Enter the Number:'))
    myNum.append(num)

print(myNum)

sum = 0

for x in myNum:
    sum = sum + x

print('Sum of the List:', sum)