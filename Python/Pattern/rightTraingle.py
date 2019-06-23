line = int(input("Enter the total line to print:"))
#for x in range(1,line+1):
#    print('* '*(x))


'''
for i in range(0, line+1):
    for j in range(0, line-i+1):
        print(' '*(j), end='')
    print('*'*(i))
''' 

for i in range(0,line+1):
    for j in range(0, line-i):
        print(' ', end='')
    print('*'*(i))