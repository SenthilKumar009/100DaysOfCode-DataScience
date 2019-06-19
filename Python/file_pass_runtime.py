from sys import argv

script, fileName = argv

txt = open(fileName)
print('The opened file {}', fileName)
print(txt.read())

fileAgain = input('Enter the file name again:')
print('The opened file {}', fileAgain)
txt_again = open(fileAgain)
print(txt_again.read())