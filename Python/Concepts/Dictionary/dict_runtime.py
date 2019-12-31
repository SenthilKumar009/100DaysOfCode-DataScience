dict = {}

num = int(input('Enter the total key-value pair:'))

for i in range(num):
    key = input("Enter the key value:")
    value = int(input('Enter the value for the Key:'))
    dict.update({key:value})

print(dict)

print(dict.get('key1'))