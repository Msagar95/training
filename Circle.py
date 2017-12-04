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
    def __gt__(self, other):
        if self.radius > other.radius:
            return True
        else:
            return False
    def __lt__(self, other):
        if self.radius < other.radius:
            return True
        else:
            return False

c1=Circle(4)
c2=Circle(5)
