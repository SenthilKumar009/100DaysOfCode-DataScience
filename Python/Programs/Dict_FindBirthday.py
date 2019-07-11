birthdays = {'SKK': '01-Jan-1987', 'Amala':'04-Jan-1986', 'SVD':'03-Nov-2014', 'SVS':'17-Oct-2016'}

while True:
    print('Enter the name:(Press enter to quit)')
    name = input()
    if name == '':
        break
    

    if name in birthdays:
        print(birthdays[name]+' is the birthday of '+name)
    else:
        print('I dont find the data in the dictionary for:'+name)
        print('Do add it in the dictionary!')
        bday = input()
        birthdays[name] = bday
        print('Data has been added!!!')