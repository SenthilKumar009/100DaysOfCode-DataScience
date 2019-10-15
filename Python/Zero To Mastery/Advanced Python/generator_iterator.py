def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            #print('Thank You!!!')
            break


special_for([1,2,3])