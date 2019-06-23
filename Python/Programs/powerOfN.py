num = int(input('Enter the Number:'))
pow = int(input('Enter the power to the number:'))

sum = 1
for i in range(0,pow):
    sum = sum * num 

print("Power to the {} of {} is {}".format(num, pow, sum))