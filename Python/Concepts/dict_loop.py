color  = {'b':"Blue", 'r':"Red", 'g': "Green"}

print("Keys:", end='')
for key in color:
    print(key, end=' ')
print()

print("Values:", end='')
for key in color:
    print(color[key], end=' ')
print()

print("Keys and Values are")
for key, value in color.items():
    print("Key:{}, Value:{}".format(key, value))