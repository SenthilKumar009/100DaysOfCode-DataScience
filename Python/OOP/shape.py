from rectangle import Rectangle
from triangle import Triangle

rect = Rectangle()
rect.set_values(100,200)
rect.set_color('Red')
print(rect.get_area())
print(rect.get_color())

tri = Triangle()
tri.set_values(100,200)
tri.set_color('Green')
print(tri.get_area())
print(tri.get_color())