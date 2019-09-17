def fun(x):
    x = 15
    print(x, id(x))

x = 10
fun(x)
print(x, id(x))