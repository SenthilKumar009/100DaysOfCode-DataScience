import math
class Circle(object):

    pi = 3.14
    def __init__(self, radius=1):
        self.radius = radius
    
    def area(self):
        return self.pi*pow(self.radius,2)
    
    def circumference(self):
        return 2*self.pi*self.radius

circle = Circle(12)

print(circle.area())
print(circle.circumference())