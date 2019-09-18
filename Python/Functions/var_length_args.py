def fun(farg, **kwargs):
    '''kwargs is used to get the key and value from it'''
    print('Formal Argument:', farg)

    for x, y in kwargs.items():
        print('Key: {}, Value:{}'.format(x, y))

fun(5, rno=10)
fun(5, rno=10, name='Senthil')