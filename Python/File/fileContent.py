import os
print(os.getcwd())
print(os.path.getsize(os.getcwd()+'/importOS.py'))
#Define the file in Python like below
print(os.path.getsize('/home/senthilkumar/Documents/100DaysOfCode-DataScience/Python/File/importOS.py'))
print(os.listdir(os.getcwd()))

totalsize = 0

for fileName in os.listdir(os.getcwd()):
    totalsize += os.path.getsize(fileName)

print("Total size of the Files from the directory "+os.getcwd()+":"+str(totalsize))

for fileName in os.listdir(os.getcwd()):
    print(fileName+':'+str(os.path.getsize(fileName)))