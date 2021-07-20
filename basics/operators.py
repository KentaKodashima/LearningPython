# Operator	Description	Example
# Operator: ==
# Description: If the values of two operands are equal, then the condition becomes true.
# Example: (a == b) is not true.

# Operator: !=
# Description: If values of two operands are not equal, then condition becomes true.
# Example: (a != b) is true.

# Operator: >
# Description: If the value of left operand is greater than the value of right operand, then condition becomes true.
# Example: (a > b) is not true.

# Operator: <
# Description: If the value of left operand is less than the value of right operand, then condition becomes true.
# Example: (a < b) is true.

# Operator: >=
# Description: If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.
# Example: (a >= b) is not true.

# Operator: <=
# Description: If the value of left operand is less than or equal to the value of right operand, then condition becomes true.
# Example: (a <= b) is true.



# ==========
# Logical operators
# ==========
# Operator: and
# Description: If both conditions are true
# Example: 'k' == 'k' and 1 == 1

# Operator: or
# Description: If one of the conditions is true
# Example: 'k' == 'k' or 1 == 1

# Operator: not
# Description: If the conditions is false
# Example: not 1 == 1



# ==========
# Useful operators
# ==========
# range() operator
# range(start,end,step)

mylist = [1,2,3]
for num in range(10):
  # Print 0 to 9
  print(num)

for num in range(2, 10):
  # Print 2 to 9
  print(num)

for num in range(0,11,2):
  # Print 0,2,4,6,8,10
  print(num)

# list() operator
# Generate a list based on the returning value of range
list(range(0,11,2))

# enumerate() operator
# Return a tuples of an index and value

# Output of the following code
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')
# (5, 'f')
# (6, 'g')
word = 'abcdefg'
for item in enumerate(word):
  print(item)

for index, char in enumerate(word):
  print(index)
  print(char)
  print('\n')

# zip() operator
# Zip together multiple lists and return as tuples

# The following code's output
# (1, 'a')
# (2, 'b')
# (3, 'c')
mylist2 = [1,2,3]
mylist3 = ['a','b','c']
for item in zip(mylist2, mylist3):
  print(item)

# The tuples are fit into the shortest list
# Any extra values will be ignored
# The following code's output
# (1, 'a', 10)
# (2, 'b', 11)
# (3, 'c', 12)
mylist4 = [10,11,12,13,14]
for item in zip(mylist2, mylist3, mylist4):
  print(item)

list(zip(mylist2, mylist3, mylist4))

# in operator
# Similar to include() in JS, it checks if a value exists in a list or an object
'x' in [1,2,3] # false
'x' in ['x', 'y', 'z'] # true
'x' in 'xyz' # true
'key' in {'key': 100} # true
d = {'key': 100}
100 in d.values # true
'key' in d.keys # true

# min/max operator
mylist5 = [10,20,30,40,100]
min(mylist5) # return 10
max(mylist5) # return 100

# Improting functions from Python's built-in library
from random import shuffle
mylist6 = [1,2,3,4,5,6,7,8,9,10]
# shuffles a list
shuffle(mylist6)

from random import randint
# Generate random int
# randint(min,max)
randint(0,100)

# Getting user input
# Asks the user for an input and store the resutl in a variable
# The result will be string
# To get an int, you need to cast using float(), int(), etc
result = input('Enter a number here: ')
int(result)
float(result)