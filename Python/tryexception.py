astr = 'TestString'
try:
    print(astr)
    istr = int(astr)
    print(istr)
except:
    istr = -1

print('done', istr)