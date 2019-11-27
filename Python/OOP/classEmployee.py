class Emplyoee:

    raise_amount = 1.05

    def __init__(self, firstName, lastName, profession, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.profession = profession
        self.salary = salary
    
    def fullName(self, firstName, lastName):
        print('{} {}'.format(self.firstName, self.lastName))

    def completeName(self):
        print('{} {}'.format(self.firstName, self.lastName))
    
    def raisePay(self):
        self.salary = int(self.salary * self.raise_amount)

emp1 = Emplyoee('Senthil Kumar', 'Kanagaraj', 'Data Scientist', 4500000)
emp2 = Emplyoee('Senthil Kumar', 'Kanagaraj', 'Data Scientist', 4500000)
emp3 = Emplyoee('Senthil Kumar', 'Kanagaraj', 'Data Scientist', 4500000)

emp1.fullName(emp1.firstName, emp1.lastName)
emp2.completeName()
Emplyoee.completeName(emp3)

print(Emplyoee.raise_amount)
print(emp1.raise_amount)

emp1.raisePay()
print(emp1.salary)