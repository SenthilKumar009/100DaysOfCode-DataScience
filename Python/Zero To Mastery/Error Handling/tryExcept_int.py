#Error handling

while True:
    try:
        age = int(input('Enter the Age:'))
        print('Age:', age)
        break
    except:
        print('Enter the Number')