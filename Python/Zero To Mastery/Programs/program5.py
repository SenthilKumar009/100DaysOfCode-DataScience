'''
    Define a class which has at least two methods:

        getString: to get a string from console input
        printString: to print the string in upper case.

    Also please include simple test function to test the class methods.
'''

class Program5(object):
    def __init__(self):
        self.val = ""

    def getString(self):
        self.val = input()
    
    def printString(self):
        return self.val.upper()

obj1 = Program5()
obj1.getString()
obj1.printString()