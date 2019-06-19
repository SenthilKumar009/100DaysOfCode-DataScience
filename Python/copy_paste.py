from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying the data from {} to {}".format(from_file, to_file))

inFile = open(from_file)
inData = inFile.read()


outFile = open(to_file, 'w+')
outData = outFile.write(inData)

#print(outFile.read())

outFile.close()
inFile.close()
