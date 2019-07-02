def myfunc(x):
    st = ''
    mylist=[]
    for letter in x:
        mylist.append(letter)
 
    for item in mylist:   
        if ord(item)%2==0:
            st += item.upper()
        else:
            st += item.lower()
    return st

print(myfunc('testing'))