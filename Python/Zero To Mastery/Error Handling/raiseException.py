#exception raise

while True:
    try:
        age = int(input('Enter the Age:'))
        10/age
        raise ValueError
    except ValueError:
        print('Please enter the Number')
        continue
    except ZeroDivisionError:
        print('Please enter higher than 0')
        break
    else:
        print('The Age is:',age)
        break
    finally:
        print('Finally Im here')
    print('Enter the Number')
