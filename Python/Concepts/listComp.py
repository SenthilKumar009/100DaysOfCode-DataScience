'''newList = [i*i for i in range(0,6) if i%2!=0]

print(newList)

squareList = [i*i for i in range(1,11)]
print(squareList)

temps = [221, 233.2, 'data', 'newdata', 1234]

new_temp = [temp for temp in temps if str(temp).isnumeric() ]
print(new_temp)

temps = [221, 233.2, -999, 1234]
newTemp = [temp/10 if temp != -999 else 0 for temp in temps]
print(newTemp)
'''

def foo(getList):
    return sum([float(data) for data in getList])

print(foo([99, -1, 96, 94, -1, -8]))