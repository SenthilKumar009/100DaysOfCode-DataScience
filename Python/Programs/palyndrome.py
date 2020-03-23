def palCheck(strng):
    newLst = []
    for ch in strng:
        if ch != ' ':
            newLst.append(ch)
    
    newString = ''
    for x in newLst:
        newString += x 
    
    print('String:', newString)
    print('Reverse String:', newString[::-1])

    if newString.lower() == newString[::-1].lower():
        print('Its a Palyndrome')
    else:
        print('Its not a Palyndrome')

palCheck('Ten animals I slam in a net')
palCheck('Hello World')

