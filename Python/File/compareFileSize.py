import zipfile, os

filePath = os.getcwd()
print(filePath)

fileZip = zipfile.ZipFile(filePath+'/example.zip')
print(fileZip.namelist())

spaminfo = fileZip.getinfo('test1.txt')
actualSize = spaminfo.file_size
compressedSize = spaminfo.compress_size

print("Actual Size of test1.txt is {} and compressed size of test1.txt is {}".format(actualSize, compressedSize))