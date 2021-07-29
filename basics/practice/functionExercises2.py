# Write a function that computes the volume of a sphere given its radius.
from fractions import Fraction
from math import pi
def vol(rad):
  return Fraction(4,3) * pi * (rad ** 3)
print(vol(2))
print('\n')
# Another approach
def vol2(rad):
  return (4/3) * pi * (rad ** 3)

# Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_bool(num,low,high):
  return num in range(low,high+1)
print(ran_bool(3,1,10))
print('\n')

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(s):
  upper = 0
  lower = 0
  for char in s:
    if char.isupper():
      upper += 1
    elif char.islower():
      lower += 1
  print(f'No. of upper case characters : {upper}')
  print(f'No. of lopwer case characters : {lower}')
up_low('Hello Mr. Rogers, how are you this fine Tuesday?')
print('\n')
# Refactored
def up_low2(s):
  d={"upper":0, "lower":0}
  for c in s:
    if c.isupper():
      d["upper"]+=1
    elif c.islower():
      d["lower"]+=1
    else:
      pass
  print("Original String : ", s)
  print("No. of Upper case characters : ", d["upper"])
  print("No. of Lower case Characters : ", d["lower"])

# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(list):
  counter = {}
  result = []
  for num in list:
    if str(num) not in counter:
      counter[str(num)] = 1
      result.append(num)
  return result
print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))
print('\n')
# Refactored
def unique_list2(lst):
  # Also possible to use list(set())
  x = []
  for a in lst:
    if a not in x:
      x.append(a)
  return x

# Write a Python function to multiply all the numbers in a list.
def multiply(numbers):  
  result = 1
  for num in numbers:
    result *= num
  return result
print(multiply([1,2,3,-4]))
print('\n')

# Write a Python function that checks whether a word or phrase is palindrome or not.
def palindrome(s):
  reversed = s[::-1]
  return s == reversed
print(palindrome('helleh'))
print(palindrome('fadjoajgopadfvgjaop'))
print('\n')
# Refactored
def palindrome(s):
  s = s.replace(' ','') # This replaces all spaces ' ' with no space ''. (Fixes issues with strings that have spaces)
  return s == s[::-1]   # Check through slicing

# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
# Pangrams are words or sentences containing every letter of the alphabet at least once. For example : "The quick brown fox jumps over the lazy dog"
import string
def ispangram(str1, alphabet=string.ascii_lowercase):
  counter = {}
  for char in str1:
    if char.lower() not in counter and char != ' ':
      counter[char.lower()] = 1
  return len(counter.keys()) == len(alphabet)
print(ispangram('The quick brown fox jumps over the lazy dog'))
# Refactored
def ispangram(str1, alphabet=string.ascii_lowercase): 
  # Create a set of the alphabet
  alphaset = set(alphabet)  
  
  # Remove spaces from str1
  str1 = str1.replace(" ",'')
  
  # Lowercase all strings in the passed in string
  # Recall we assume no punctuation 
  str1 = str1.lower()
  
  # Grab all unique letters in the string as a set
  str1 = set(str1)
  
  # Now check that the alpahbet set is same as string set
  return str1 == alphaset