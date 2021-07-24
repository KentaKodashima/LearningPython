# WARMUP SECTION:

# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5
def lesser_of_two_evens(a,b):
  if a % 2 == 0 and b % 2 ==0:
    return min(a,b)
  else:
    return max(a,b)
print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))
print('\n')

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False
def animal_crackers(str):
  words = str.split()
  return words[0][0] == words[1][0]
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))
print('\n')

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False
def makes_twenty(a,b):
  if a == 20 or b == 20:
    return True
  elif a + b == 20:
    return True
  return False
print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))
print('\n')



# LEVEL 1 PROBLEMS

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald
def old_macdonald(name):
  result = ''
  current = 0
  for char in name:
    if current == 0 or current == 3:
      result += char.capitalize()
    else:
      result += char
    current += 1
  return result
print(old_macdonald('macdonald'))
print('\n')

# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'
def master_yoda(text):
  words = text.split()
  current = len(words) - 1
  result = ''
  while (current >= 0):
    result += words[current]
    result += ' '
    current -= 1
  return result
print(master_yoda('I am home'))
print(master_yoda('We are ready'))
print('\n')

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True
def almost_there(n):
  pass
# print(almost_there(90))
# print(almost_there(104))
# print(almost_there(150))
# print(almost_there(209))
# print('\n')

# LEVEL 2 PROBLEMS¶

# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False
def has_33(nums):
  prev = False
  for num in nums:
    if num == 3 and prev == True:
      return True
    elif num == 3 and prev == False:
      prev = True
    else:
      prev = False
  return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
print('\n')

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
def paper_doll(text):
  result = ''
  for char in text:
    result += char * 3
  return result
print(paper_doll('Hello'))
print(paper_doll('Mississippi'))
print('\n')

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19
def blackjack(a,b,c):
  sum = a + b + c
  if sum <= 21:
    return sum
  else:
    if a == 11 or b == 11 or c == 11:
      sum -= 10
      if sum <= 21:
        return sum
  return 'BUST'
print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))
print('\n')

# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14
def summer_69(arr):
  sum = 0
  ignore = False
  for num in arr:
    if num == 6:
      ignore = True
    elif num == 9:
      ignore = False
    elif ignore == False:
      sum += num
  return sum
print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

