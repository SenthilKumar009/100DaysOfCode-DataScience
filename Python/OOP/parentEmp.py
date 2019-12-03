class Employee:
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullName(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_employees(self):
        for emp in self.employees:
            print('-->', emp.fullName())

dev_1 = Developer('Senthil', 'Kumar', 2100000, 'Python')
dev_2 = Developer('Guna', 'Raj', 2100000, 'Statistics')

mgr1 = Manager('Sue', 'Smith', '900000', [dev_1])

print(mgr1.email)

mgr1.print_employees()

#print(dev_1.fullName())
#print(dev_1.email)
#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)
#print(dev_1.prog_lang)