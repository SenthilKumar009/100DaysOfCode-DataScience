from sys import argv
from os.path import exists

script, from_file, to_file = argv

print('Copying data from {} to {} file'.format(from_file, to_file))