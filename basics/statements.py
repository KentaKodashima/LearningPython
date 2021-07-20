# Only the Python unique features are noted

# if/else statement
# No curly braces unline in JS
a = 3
b = 2

if a > b:
  print('true')
elif a == b:
  print('true')
else:
  print('false')

# for loop
nums = [0,1,2,3,4]
sum = 0
for num in nums:
  sum += num

str = 'Hello world'
for char in str:
  print(char)

for _ in str:
  print('every single char')

tup = (1,2,3)
for item in tup:
  print(item) # 1 2 3

tups = [(1,2),(3,4),(5,6),(7,8)]
for item in tups:
  print(item) # (1,2) (3,4) (5,6) (7,8)
for (a, b) in tups:
  print(a) # 1 3 5 7
  print(b) # 2 4 6 8

obj = {'0': 1, '1': 2, '2': 3}
for val in obj.values:
  print(val) # 1 2 3

# Keywords for loops
# break: Ends the loop just like in JS

# continue: Goes to the top of the closest enclosing loop
str2 = 'Hello'
for char in str2:
  if char == 'l':
    continue
    # Continue to the next char without printing 'l'
  print(char)

# pass: Used to have empty content inside a loop
x = [1,2,3]
for item in x:
  pass