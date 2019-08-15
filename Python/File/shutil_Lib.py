import os
import shutil

currentPath = os.getcwd()
source = currentPath + '/TestFileFolder/test1.txt'
dest = currentPath + '/CopyFolder'

print(source)
shutil.copy(source, dest)

#dest = shutil.copy(currentPath+'/TestFileFolder/test1.txt', currentPath+'/CopyFolder')