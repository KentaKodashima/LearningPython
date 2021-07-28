# Write a function that computes the volume of a sphere given its radius.
def vol(rad):
  pass

# Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_bool(num,low,high):
  return num in range(low,high)
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