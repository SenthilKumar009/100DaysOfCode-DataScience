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

    @classmethod
    def increase_amount(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, empStr):
        first, last, job, pay = empStr.split('-')    
        return cls(first, last, job, pay)

emp1 = Emplyoee('Senthil Kumar', 'Kanagaraj', 'Data Scientist', 4500000)
emp2 = Emplyoee('Senthil Kumar', 'Kanagaraj', 'Data Scientist', 4500000)
emp3 = Emplyoee('Senthil Kumar', 'Kanagaraj', 'Data Scientist', 4500000)

emp1.fullName(emp1.firstName, emp1.lastName)
emp2.completeName()
Emplyoee.completeName(emp3)

print(Emplyoee.raise_amount)
print(emp1.raise_amount)

Emplyoee.increase_amount(1.08)

print(Emplyoee.raise_amount)
print(emp1.raise_amount)
print(Emplyoee.raise_amount)

#emp1.raisePay()
#print(emp1.salary)

emp_str_1 = 'Senthil-Kumar-DataScientist-4500000'
emp_str_2 = 'Senthil-Kumar-IoT Engineer-5400000'
emp_str_3 = 'Senthil-Kumar-Entrepreneuier-6300000'

newEmp1 = Emplyoee.from_string(emp_str_1)
print(newEmp1.fullName(newEmp1.firstName, newEmp1.lastName))
print(newEmp1.salary)