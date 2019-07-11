import math
class Circle:

    pi = 3.14
    def __init__(self, radius=1):
        self.radius = radius
    
    def area(self):
        return self.pi*pow(self.radius,2)
    
    def circumference(self):
        return 2*self.pi*self.radius

c1 = Circle(12)

print(c1.area())
print(c1.circumference())