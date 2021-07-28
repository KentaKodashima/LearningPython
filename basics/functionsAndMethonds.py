# Only the Python unique features are noted

# A function in Python can be defined with the keyword 'def'
def say_hello():
  print('hello')
  print('how')
  print('are')
  print('you')

def say_name(name):
  print(f'hello {name}')

def add(num1, num2):
  return num1 + num2

# Tuple unpacking with Python functions
work_hours = [('Abby',100),('Billy',400),('Cassie',100)]
def employee_check(work_hours):
  current_max = 0
  employee_of_month = ''

  for employee,hours in work_hours:
    if hours > current_max:
      current_max = hours
      employee_of_month = employee
    else:
      pass

  return (employee_of_month,current_max)
# The function returns a tuple
# It can be unpacked as below
name,hours = employee_check(work_hours)



# ==========
# Arguments
# ==========
# *: args
# **: kwargs = keyword args

# The function below cam take arbitary numbers of arguments
# Args are treated as tuples inside the funciton
def myfunc(*args):
  return sum(args) * 0.05
myfunc(40,60,100)
myfunc(40,60,100,200)

# THe function below can also take arbitary numbers of arguments
# The args need to have a keyword
# Insted of tuples, args would be dictionaries
def myfunc(**kwargs):
  if 'fruit' in kwargs:
    print(f'My fruit of choice is {kwargs["fruit"]}')
myfunc(fruit='apple',veggie='onions')

def myfunc(*args,**kwargs):
  print(f'I would like {args[0]} {kwargs["food"]}')
myfunc(10,20,30,food='pizza',fruit='apple')



# ==========
# Lambda expressions
# ==========
def slicer(str):
  if len(str) % 2 == 0:
    return 'Even'
  else:
    return 'Odd'
names = ['Andy', 'Eve', 'Sally']
results = list(map(slicer,names))

def is_even(num):
  return num % 2 == 0
nums = [1,2,3,4,5,6]
even_nums = list(filter(is_even,nums))
for n in filter(is_even,nums):
  print(n)

# Lambda is anonymous functions
square = lambda num: num ** 2
square(5)

# Lambda is used when you want to have an one time function
list(map(lambda num: num ** 2, nums))
list(map(lambda x: x[::-1], names))
list(filter(lambda num: num % 2 == 0, nums))



# ==========
# Scopes
# ==========
# Global variables are accessible with the 'global' keyword 
# Though you can do this, it's a bad practice
# It's better to take the global variables as arguments because it's easier to debug
x = 50
def func():
  global x
  print(f'X is {x}')
  x = 200
  print(f'Locally changed global X to {x}')
func()
print(x) # now it's 200