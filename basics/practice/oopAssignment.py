from math import pi

# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
class Line:
  def __init__(self,coor1,coor2):
    self.coor1 = coor1
    self.coor2 = coor2
  
  def distance(self):
    x1,y1 = self.coor1
    x2,y2 = self.coor2
    return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
  
  def slope(self):
    x1,y1 = self.coor1
    x2,y2 = self.coor2
    return (y2 - y1) / (x2 - x1)

# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.distance()) # 9.433981132056603
print(li.slope()) # 1.6

class Cylinder:
  def __init__(self,height=1,radius=1):
    self.height = height
    self.radius = radius
      
  def volume(self):
    # Volume of a cylinder: pi * r**2 * h
    return pi * (self.radius ** 2) * self.height
  
  def surface_area(self):
    # Surface area of a cylinder: 2*pi*r*h + 2*pi*r**2
    return (2 * pi * self.radius * self.height) + (2 * pi * (self.radius ** 2))

c = Cylinder(2,3)
print(c.volume()) # should be 56.52
print(c.surface_area()) # should be 94.2