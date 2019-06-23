n = int(input("Enter the number:"))

f1 = 0
f2 = 1
itr = 1

while itr<=n:
    if(itr == 1):
        print(str(f1)+' ', end='')
        itr += 1
    elif(itr == 2):
        print(str(f2)+' ', end='')
        itr += 1
    else:
        f=f1+f2
        print(str(f)+' ', end='')
        f1 = f2
        f2 = f
        itr += 1
print()
