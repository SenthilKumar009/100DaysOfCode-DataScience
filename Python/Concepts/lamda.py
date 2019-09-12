x = lambda a: a+10
print(x(5))

sum = lambda a,b,c : a+b+c
print(sum(12,12,12))

def myfun(n):
    return lambda a : a * n

mysum = myfun(3)
print(mysum(10))