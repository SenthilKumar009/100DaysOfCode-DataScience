def ask_for_int():

    while True:
        try:
            result = int(input('Enter the number:'))
        except:
            print('You have entered the non-integer value!!!')
            continue
        else:
            print('You have entered: ', result)
            break
        finally:
            print('End of try/Except block!!!')
            print('It runs always at the end!!!')

ask_for_int()

def intArray_check():
    try:
        for i in ['a', 'b', 'c', 3, 4]:
            print(i**2)
    except TypeError:
        print('Number is not avialble to make it square')
    finally:
        print('At the end I run')

intArray_check()

def divByZero():
    try:
        print(2/0)
    except:
        print('Return division by Zero')
    finally:
        print('At the end I run')

divByZero()