''' Write a program that calculates and prints the value according to the given formula:
    Q = Square root of [(2 * C * D)/H]
    Following are the fixed values of C and H:
    C is 50. H is 30.
    D is the variable whose values should be input to your program in a comma-separated sequence.
    For example Let us assume the following comma separated input sequence is given to the program:
    100,150,180
    The output of the program should be:
    18,22,24
'''
import sys
import math

values = []
n = int(input('Enter the total values:'))
c = 50
h = 30
for i in range (0, n):
    val = int(input())
    values.append(val)

for d in values:
    q = math.sqrt((2*c*d)/h)
    print(math.trunc(q), end = ',')
print('\b')