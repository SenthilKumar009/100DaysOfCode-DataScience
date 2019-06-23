n = int(input("Enter the number:"))

count = 2
f1 = 0
f2 = 1

while count<n:
    count += 1
    f = f1+f2
    f1 = f2
    f2 = f
    print(count,':',f)

print(count, 'th Fibonacci Number is:',f)