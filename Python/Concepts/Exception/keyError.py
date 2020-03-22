dict = {'a':'b', 'b':'c', 'c':'d'}
ch = 'a'

try:
    while True:
        ch = dict[ch]
        print(ch)
except KeyError:
        print('No Such Key:',ch)