my_list = list(range(4,9,2))

print(my_list)

my_list[0] = 'Four'
print(my_list)

my_list.append('Seven')
print(my_list)

my_list.pop()
print(my_list)

my_list.pop(0)
print(my_list)

my_list.append('SKK')
my_list.append('Data Scientist')
my_list.append('iOS Developer')

print(my_list)

a = [1, 2, 3, 4, 5]
b = [10, 20, a,['a', 'b', 'c']]

print(a)
print(b)

print(b[2][2])
print(b[3][0])

#Print Matrix

mat = [[1,2,3],[4,5,6],[7,8,9]]

for row in mat:
    for col in row:
        print(col, end=' ')
    print()


square = []
for i in range(1,11):
    square.append(i**2)

print(square)

x = [1,2,3]
y = [10,11,12]
sum = [i+j for i in x for j in y]

print(sum)