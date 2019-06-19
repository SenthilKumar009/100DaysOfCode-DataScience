xFile = input('enter the file to process:')
openFile  = open(xFile, 'w')

print('Truncating the file...')
openFile.truncate()

#print(openFile.read())

print("Getting data to update in the file")
line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

openFile.write(line1+'\n')
openFile.write(line2+'\n')
openFile.write(line3+'\n')