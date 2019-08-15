import zipfile, os

filePath = os.getcwd()
print(filePath)

newZip = zipfile.ZipFile('newZip.zip', 'w')
newZip.write(filePath+'/test1.txt', compress_type= zipfile.ZIP_DEFLATED)
newZip.close()