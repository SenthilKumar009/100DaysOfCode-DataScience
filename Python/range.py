data = [1,2,3,4,5]

#for i in data:
#    print(i)

#print('List length:', len(data))
#for i in range (0,len(data)):
#    print('Value in {} index is {}'.format(i, data[i]))

'''event_list = range(2,10,2)

for i in event_list:
    print(i) '''

#the below function will convert the given chareturn the specified char to the
'''
def char_range(char1, char2):
    for char in range(ord(char1), ord(char2)+1):
        yield (char)

for letter in char_range('a','z'):
    print(chr(letter))
'''

for i in range(5,0,-1):
    print(i)