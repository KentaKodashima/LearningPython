# Answer these 3 questions without typing code. Then type code to check your answer.
#   What is the value of the expression 4 * (6 + 5)
#     A: 44
#   What is the value of the expression 4 * 6 + 5
#     A: 29
#   What is the value of the expression 4 + 6 * 5
#     A: 50

# ==========
# General
# ==========
# Numbers:
#   Any integers. Can be used with mathematical operators.

# Strings:
#   A string can be specified with '' or "".
#   Can be accessed with index numbers.
#   Use slicing operator to get substrings.
#   Strings are immutable.

# Lists:
#   A list is a collection of values.
#   Can be accessed with index numbers.
#   Lists are mutable.

# Tuples:
#   A tuple is a collection of values.
#   Tuples are immutable.

# Dictionaries:
#   A dictionary is a collection of key value pairs.
#   Can be accessed with the key name.
#   Dicts are mutable.



# ==========
# Numbers
# ==========
# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
100.25 * 1
100.25 / 1
100.25 ** 1
100 + 0.25
100.50 - 0.25

# Answer these 3 questions without typing code. Then type code to check your answer.
4 * (6 + 5) # 44
4 * 6 + 5 # 29
4 + 6 * 5 # 34

# What is the type of the result of the expression 3 + 1.5 + 4?
# A: 8.5

# What would you use to find a number’s square root, as well as its square?
# Square root: 100 ** 0.5
# Square: 100 ** 2



# ==========
# Strings
# ==========
# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s = 'hello'
# Print out 'e' using indexing
print(s[1])

# Reverse the string using slicing
print(s[::-1])

# Given the string hello, give two methods of producing the letter 'o' using indexing.
# Method 1:
print(s[-1])

# Method 2:
print(s[4])



# ==========
# Lists
# ==========
# Build this list [0,0,0] two separate ways.
list1 = [0,0,0]

# Method 2:
list2 = []
list2.append(0)
list2.append(0)
list2.append(0)

[0] * 3

print(list2)

# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'

# Sort the list below:
list4 = [5,3,4,6,1]
list4.sort()

# sorted(list4) returns the sorted list unlike .sort()



# ==========
# Dictionaries
# ==========
# Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
d['simple_key']

d2 = {'k1':{'k2':'hello'}}
d2['k1']['k2']

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
d3['k1'][0]['nest_key'][1][0]

d4 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
d4['k1'][2]['k2'][1]['tough'][2][0]

# Can you sort a dictionary? Why or why not?
#   No, because it's unordered.



# ==========
# Tuples
# ==========
# What is the major difference between tuples and lists?
#   Tuples are immutable while lists are mutable.

# How do you create a tuple?
#   Using parentheses: tuple = (0,1,2)



# ==========
# Sets
# ==========
# What is unique about a set?
#   Each element in a set is guranteed to be unique

# Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
set = set(list5)



# ==========
# Bools
# ==========
# What will be the resulting Boolean of the following pieces of code (answer fist then check by typing it in!)

# Answer before running cell
2 > 3 # false

# Answer before running cell
3 <= 2 # false

# Answer before running cell
3 == 2.0 # false

# Answer before running cell
3.0 == 3 # true

# Answer before running cell
4**0.5 != 2 # false

# What is the boolean output of the cell block below?
# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
l_one[2][0] >= l_two[2]['k1'] # false