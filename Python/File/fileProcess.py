import os
openFile = open('/home/senthilkumar/Desktop/track.txt', 'a')
openFile.write('Jus testing this functionality!!!')
openFile.close
openFile = open('/home/senthilkumar/Desktop/track.txt')
content = openFile.read()
openFile.close()
print(content)