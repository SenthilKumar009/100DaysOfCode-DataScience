line = int(input("Enter the total line to print:"))

for i in range(1,line+1):
    for j in range (i,line):
        print(' ', end='')
    
    for k in range (0, 2*i-1):
        print('*', end='')
    
    print()