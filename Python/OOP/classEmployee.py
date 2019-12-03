class Emplyoee:

    raise_amount = 1.05

    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.email = firstName + '.' + lastName + '@email.com'
        self.salary = salary
    
    def fullName(self, firstName, lastName):
        print('{} {}'.format(self.firstName, self.lastName))

    def raisePay(self):
        self.salary = int(self.salary * self.raise_amount)

    @classmethod
    def increase_amount(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, empStr):
        first, last, pay = empStr.split('-')    
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = Emplyoee('Senthil Kumar', 'Kanagaraj', 4500000)
emp2 = Emplyoee('Senthil Kumar', 'Kanagaraj', 4500000)
emp3 = Emplyoee('Senthil Kumar', 'Kanagaraj', 4500000)

emp1.fullName(emp1.firstName, emp1.lastName)
emp2.fullName(emp2.firstName, emp2.lastName)

print(Emplyoee.raise_amount)
print(emp1.raise_amount)

emp1.raisePay()
print(emp1.salary)

Emplyoee.increase_amount(1.08)

print(Emplyoee.raise_amount)
print(emp1.raise_amount)

emp1.raisePay()
print(emp1.salary)

emp_str_1 = 'Senthil-Kumar-4500000'
emp_str_2 = 'Senthil-Kumar-5400000'
emp_str_3 = 'Senthil-Kumar-6300000'

newEmp1 = Emplyoee.from_string(emp_str_1)
print(newEmp1.email)
#print(newEmp1.fullName(newEmp1.firstName, newEmp1.lastName))
print(newEmp1.salary)

import datetime
my_date = datetime.date(2020, 3, 6)
print(Emplyoee.is_workday(my_date))