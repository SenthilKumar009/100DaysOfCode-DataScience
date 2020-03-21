'''
def greet(lang):
    if(lang == 'es'):
        return('Holo')
    elif(lang == 'fr'):
        return('Bonjur')
    else:
        return('Hello')

print(greet('en'), 'Maxwell')
print(greet('es'), 'Steffy')
print(greet('fr'), 'Senthil')

list = ['a', 'b', 'c', 'd', 'e']
def list(lst):
    del lst[3]
    lst[3] = 'x'

print(list(list))

def fun(x):
    x += 1
    return x

x = 2
x = fun(x+1)
print(x)

tup = (1,2,3,4)
tup[1] = tup[1] + tup [0]
#tup = tup[0]
print(tup)


def fun(x):
    global y
    y = x * x
    return y

fun(2)
print(y)
'''

dct = {}
dct['1'] = (1,2)
dct['2'] = (2,1)

for x in dct.keys():
    print(dct[x][1], end='')
'''
def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2

print(fun(fun(2)))

x = float(input())
y = float(input())

print(y ** (1/x))

print(1//5 + 1/5)

lst = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        print(lst[r][c])
        if lst[r][c] % 2 != 0:
            print('#')

lst = [1,2]
for v in range(2):
    lst.insert(-1, lst[v])

print(lst)

def fun(inp=2, out=2):
    return inp * out

print(fun(out=2))

x = 1
y = 2
x,y,z = x,x,y
z,y,z = x,y,z

print(x,y,z)

i = 0
while i < i + 2:
    i += 1
    print('*')
else:
    print('*')

a = 1
b = 0
a = a^b
b = a^b
c = a^b

print(a,b)

def fun1(a):
    return None

def fun2(a):
    return fun1(a) * fun1(a)

#print(fun2(2))
print(1//2)

nums = [1,2,3]
vals = nums
del vals[:]
print(nums)
print(vals)

lst = [i for i in range(-1,-2)]
print(lst)

dd = {'1':'0', '0':'1'}
for x in  dd.values():
    print(x, end='')

def func(a,b=0):
    return a**b

print(func(b=2))

lst = [x*x for x in range(5)]

def fun(lst):
    del lst[lst[2]]
    return lst

print(fun(lst))
'''
tup = (1,2,4,8)
tup[1] = tup[1] + tup[0]
#print(tup)
#tup = tup[-1]
print(tup)
