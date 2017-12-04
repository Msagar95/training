import math
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def setRadius(self,radius):
        self.radius = radius
    def getRadius(self):
        return self.radius
    def area(self):
        ar=math.pi*((self.radius)**2)
        return(ar)
    def __add__(self, other):
        radius=self.radius+other.radius
        return radius

c1=Circle(4)
c2=Circle(5)

print("Area of circle-1: ", c1.area())
print("Area of circle-2: ", c2.area())
print("Sum of radii: ", c1+c2)