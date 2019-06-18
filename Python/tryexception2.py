x  = input('Enter the number:')
try:
    ival = int(x)
except:
    ival = -1

if ival > 0:
    print('Its a Numer')
else:
    print('Not a number')
