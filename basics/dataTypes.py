# Only the Python unique features are noted

# ==========
# String
# ==========
mystring = "abcdefghijklmn"

# String can be accessed with index specified by []
# Colon(:) is used as a slice operator
# Slicing syntax is [start:end:step]:
#   start: The start index (included)
#   end: The end index (excluded)
#   step: How many indices should be skipped
mystring[-1] # The last char which is "n"
mystring[2:] # Start from the second index to the end "cdefghijklmn"
mystring[:3] # Start from the first char to the second index "abc"
mystring[3:6] # Start from "def"
print(mystring[::2]) # acegikm
mystring[::-1] # Reverse string

# Strings are immutable
name = 'Sam'
# name[0] = 'P' doesn't work
# You should concatenate the strings instead
last_letters = name[1:]
new_name = 'P' + last_letters # 'Pam'

# String concatenation
# Can be multiplied
letter = 'z'
letter * 10 # 'zzzzzzzzzz'

# String interpolation
# Insert a string using .format()
# The curly braces are replaced with the variable
print('this is a string {}'.format('INSERTED'))
# You can pass an index of a variable
print('this {2} {1} {0}'.format('fox', 'brown', 'quick')) # The quick brown fox
print('this {q} {b} {f}'.format(f='fox',b='brown',q='quick')) # The quick brown fox


# ==========
# Formatting
# ==========

# Float formatting
# {value:width.precision f}
#   value: base value
#   width: the length of the string to be
#   precision: the length of the numbers after the decimal point
result = 100/777 # 0.1287001287001287
print('The result was {r:1.3f}'.format(r=result)) # 0.129

# f_string
name = 'Jose'
print(f'The name is {name}')


# ==========
# List
# ==========
my_list = ['one', 2, 3.1]
len(my_list) # 3

# THe slicing operator can be used with the lists too
my_list[0] # 'one'
my_list[1:] # 2, 3.1

# Lists can be concatenated
another_list = ['four', 5]
new_list = my_list + another_list

# Unlike strings, elements are mutable
new_list[0] = 1
new_list.append(6)


# ==========
# Tuples
# ==========
t = (1,2,3)
type(t) # Tuple
list = [1,2,3]
type(list) # List

t = ('a', 'a', 'b')
t.count('a') # 2
t.index('a') # 0

# Unlike lists, elements are immutable in tuples
# t[0] = 'new' doesn't work


# ==========
# Sets
# ==========
# Sets are unordered collections of unique elements.
my_set = set()
my_set.add(1)
my_set.add(2)
# my_set.add(1) will be {1,2}

# A list can be casted to a set
# Duplicates are removed
list_to_cast = [1,1,1,1,1,2,2,2,2,3,3,3]
set(list_to_cast) # {1,2,3}