import os

print(os.getcwd())
print(os.listdir(os.getcwd()))
print(os.path.join('c', 'python'))
print(os.path.join('home/documents/personal/resume', 'resume.txt'))

print(os.path.abspath('\\importOS.py'))

calcFilePath = 'C:\\Windows\\System32\\calc.exe'
print(os.path.split(calcFilePath))
print(os.path.join('C:\\Windows\\System32\\', 'calc.exe'))

#os.makedirs('/home/senthilkumar/Documents/100DaysOfCode-DataScience/Python/File/TestFileFolder')