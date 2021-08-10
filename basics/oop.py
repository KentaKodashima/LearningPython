class Dog():
  species = 'mammal'

  def __init__(self,breed,name,spots) -> None:
    # String
    self.breed = breed
    # String
    self.name = name
    # Bool
    self.spots = spots

  def bark(self,number):
    print(f'Woof! My name is {self.name}, number {number}')

my_dog = Dog('lab','John',False)
my_dog.bark(1)


class Circle():
  pi = 3.14

  def __init__(self,radius):
    self.radius = radius
    # The name of the class can be used insted of 'self'
    self.area = radius * radius * Circle.pi
  
  def get_circumference(self):
    return self.radius * self.pi * 2