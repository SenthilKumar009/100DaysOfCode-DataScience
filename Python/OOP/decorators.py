class Employee:
    raise_amt = 1.05

    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    @fullName.setter
    def fullName(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    

emp1 = Employee('Jhon', 'Smith')
print(emp1.first)
print(emp1.email)
emp1.first = 'Steven'
print(emp1.fullName)

emp1.fullName = 'David Warner'
print(emp1.fullName)
print(emp1.email)