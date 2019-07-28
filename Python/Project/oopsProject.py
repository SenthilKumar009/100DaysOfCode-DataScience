import math
class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1,x2 = self.coor1
        y1,y2 = self.coor2
        print(((x2-x1)**2) + ((y2-y1)**2)**0.5)
        #/print(math.sqrt((self.coor1[1]-self.coor1[0])**2 + (self.coor2[1]-self.coor2[0])**2))
    
    def slope(self):
        #print("X1: {}, X2: {}, Y1: {}, Y2:{}".format(self.coor1[0], self.coor1[1], self.coor2[0], self.coor2[1]))
        print( (self.coor2[1]-self.coor2[0]) / (self.coor1[1]-self.coor1[0]) )

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
li.distance()
li.slope()

class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        print(math.pi*self.radius**2*self.height)
    
    def surface_area(self):
        print((2*math.pi*self.radius*self.height)+(2*math.pi*self.radius**2))

c = Cylinder(2,3)
c.volume()
c.surface_area()