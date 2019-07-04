class Emp:
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    def display(self):
        print('Id=', self.id)
        print('Name=', self.name)
        print('Salary=', self.sal)
    
class MyClass:
    @staticmethod
    def myMethod(e):
        e.sal += 1000
        e.display()

e = Emp(9, 'SKK', 5700000)
MyClass.myMethod(e)