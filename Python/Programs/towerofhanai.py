def towers(n, a, c, b):

    if n == 1:
        print('Move disk %i from pole %s to pole %s' %(n, a, c))
    else:
        towers(n-1, a, b, c)
        print('Move disk %i from pole %s to pole %s' %(n, a, c))
        
        towers(n-1, b, c, a)

n = int(input('Enter the disk count:'))
towers(n, 'A', 'C', 'B')