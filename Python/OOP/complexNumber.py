class ComplexNumber:
    def __init__(self, r = 0, i = 0):
        self.real = r
        self.imag = i
    
    def getData(self):
        print("{0}+{1}j".format(self.real, self.imag))

c1 = ComplexNumber(2,3)
#deleting imag attribute from Object c1
del c1.imag
c1.getData()

c2 = ComplexNumber(5)
#delete the object c2
del c2
c2.getData()
