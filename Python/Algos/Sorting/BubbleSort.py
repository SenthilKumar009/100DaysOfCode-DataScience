numbers = []
print('Enter the total Numbers:', end='')
count = int(input())

for i in range (count):
    val  = int(input())
    numbers.append(val)

print('Before Sorting:', end='')
print(numbers)

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] > numbers [j]:
            numbers[i], numbers [j] = numbers[j], numbers[i]
'''
for i in range(len(numbers)-1):
    if numbers[i] > numbers[i+1]:
        numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
'''
print('After Sorting:', end='')
print(numbers)