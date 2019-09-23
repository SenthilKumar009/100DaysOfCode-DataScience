def newfunc(a):
    return a*a

x = map(newfunc, (1,2,3,4)) #x is the map object
print(x)
print(set(x))