def packing(*args):
    sum = 0
    for x in range (0, len(args)):
        sum += args[x]
    
    return sum

print(packing(1,2,3,4,5))