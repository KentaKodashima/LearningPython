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



# ==========
# Inheritance
# ==========
class Animal():
  def __init__(self) -> None:
      print('Animal initialized')

  def eat(self):
    print('I am eating')

  def who_am_i(self):
    print('I am an animal')

class Cat(Animal):
  def __init__(self):
      Animal.__init__(self)
      print('Cat initialized')
  def who_am_i(self):
    print('I a cat')

my_cat = Cat()
my_cat.eat()
my_cat.who_am_i()



# ==========
# Polymorphism
#
# Different objects and share the same method name.
# ==========
class Sheep():
  def __init__(self, name):
    self.name = name
  
  def speak(self):
    return self.name + ' says baa'

class Bird():
  def __init__(self,name):
    self.name = name

  def speak(self):
    return self.name + ' says I can speak'

john = Sheep('John')
mike = Bird('Mike')
for animal_class in [john, mike]:
  print(type(animal_class))
  print(type(animal_class.speak()))

def animal_speak(animal):
  print(animal.speak())

animal_speak(john)
animal_speak(mike)



# ==========
# Abstract class
# 
# Never be initialized. It acts as a base class.
# ==========
class Mammal():
  def __init__(self, name):
    self.name = name

  def speak(self):
    raise NotImplementedError('Subclass must implement this abstract method.')

class Dingo(Mammal):
  def speak(self):
    return self.name + ' says woof'

bob = Dingo('Bob')



# ==========
# Special methods
# ==========
class Book():

  def __init__(self,title,author,pages):
    self.title = title
    self.author = author
    self.pages = pages
  
  # Str representation of the class
  def __str__(self) -> str:
    return f'{self.title} by {self.author}'

  def __len__(self):
    return self.pages

  def __del__(self):
    print('A book obj has been deleted')

book = Book('Python', 'Jose', 200)
print(book) # Print the str representation
print(len(book)) # 200
del book # Delete a variable
