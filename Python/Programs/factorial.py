num = int(input("Enter the number to find Factorial!:"))

fact = 1
if(num == 1):
    print('Factorial of the given Number:', fact)
else:
    for i in range(num, 1, -1):
        fact = fact * i
    print('Factorial of the given Number:', fact)