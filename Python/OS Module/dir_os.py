import os

print(os.getcwd())
os.chdir('/home/skk_thenotorious/Desktop')
#print(os.getcwd())

#print(os.environ.get('HOME'))
filePath = os.path.join(os.environ.get('HOME'), 'test.txt')
#print(filePath)

print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))