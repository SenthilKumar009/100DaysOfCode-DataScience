#myList  = [6,2,1,4,5,2]
#print(myList[3:5])

#print()
'''
i = 0
while i <= 5:
    i+=1
    if i%2 == 0:
        break
    print('*')

x = 1
x = x==x
print(x)

a = 1
b = 0
c = a & b
d = a | b
e = a ^ b
print(c,d,e) 

t = [[3-i for i in range(3)] for j in range(3)]
s= 0
for i in range(3):
    s+=t[i][i]

print(s)

var  = 1
while var <10:
    print('#')
    var = var << 1

vals = [0,1,2]
vals.insert(0,1)
del vals[1]
print(vals)

i = 0
while i <= 3:
    i +=2
    print('*')

lst = [3,1,-2]
print(lst[lst[-1]])

z = 10
y = 0
x = y < z and z > y or y > z and z < y
print(x)

nums = [1,2,3,4]
print(nums)
vals = nums[-3:-2]
print(vals)


for i in range(1):
    print('%')
else:
    print('%')
'''

lst = [[0,1,2,3] for i in range(2)]
print(lst[2][0])