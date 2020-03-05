import os

print('Current Working Directory:{}'.format(os.getcwd()))
#print(os.listdir(os.getcwd()))
print('Join the folder and File:{}'.format((os.path.join('c', 'python'))))
print('Join Parent folder and File:{}'.format(os.path.join('/home/senthilkumar/Documents/Personal/resume', 'resume.txt')))

print('Absolute path of the Current Folder:{}'.format(os.path.abspath('.')))
print('Absolute path of the File:{}'.format(os.path.abspath('../importOS.py')))

print(os.path.relpath('.'))
print('Relative Path:{}'.format(os.path.relpath('/home/senthilkumar/Documents/100DaysOfCode-DataScience/Python/File/importOS.py')))
print('Relative Path:{}'.format(os.path.relpath('/home/senthilkumar/Documents/100DaysOfCode-DataScience/Python/File/','importOS.py')))


calcFilePath = '/home/senthilkumar/Documents/100DaysOfCode-DataScience/Python/File/importOS.py'
print(os.path.split(calcFilePath))

print(os.path.dirname(calcFilePath))
print(os.path.basename(calcFilePath))

#print(os.path.join('C:\\Windows\\System32\\', 'calc.exe'))

#os.makedirs('/home/senthilkumar/Documents/100DaysOfCode-DataScience/Python/File/TestFileFolder')