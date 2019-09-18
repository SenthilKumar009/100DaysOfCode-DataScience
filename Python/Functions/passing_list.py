def calculate(lst):
    '''find the total and average'''
    n = len(lst)
    sum = 0
    for i in lst:
        sum += i
        
    avg = sum/n
    return sum, avg

print('Enter the inputs with space:')

lst = [int(x) for x in input().split()]

x,y = calculate(lst)
print('Sum of the give Numbers:', str(x))
print('Average of the give Numbers:', str(y))
