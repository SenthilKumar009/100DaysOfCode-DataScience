xFile = input('Enter the File Name:')

try:
    fOpen = open(xFile)
except:
    print("File not found and cannot be opened", xFile)
    quit()

count = 0

for line in xFile:
    count = count + 1

print('Total line in the File:', count)