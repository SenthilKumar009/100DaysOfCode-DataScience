line = int(input("Enter the total line to print:"))
for x in range(1,line+1):
    for y in range(1, x+1):
        print('* ', end="")
    print()