# Three keywords for error handling
#   try: The code block to be attempted
#   except: The code block to be executed in case there is an error in try block
#   finally: The code block to be executed at the end, regardless of an error

def add(n1,n2):
  print(n1+n2)

number1 = 10
number2 = input('Please provide a number: ')

try:
  # result = add(number1, number2)
  result = 10 + 10
except:
  print('There is an error. Please cHeck if your input is really a number.')
else:
  # Executed when there is no error
  print('Addition was successful.')
  print(result)

# Python's built-in exceptions:
#   https://docs.python.org/3/library/exceptions.html
try:
  f = open('testfile', 'r')
  f.write('write a test line')
except TypeError:
  print('There was a type error.')
except OSError:
  print('There was an OS Error.')
except:
  print('All other exceptions.')
finally:
  print('It is always executed at the end.')

def ask_for_int():
  while True:
    try:
      result = int(input('Please provide number: '))
    except:
      print('Whooops. That is not a number.')
      continue
    else:
      print('Thank you for your input.')
      break
    finally: # Finally can be removed
      print('End of try/except/finally')
      print('This is always be executed at the end.')

ask_for_int()