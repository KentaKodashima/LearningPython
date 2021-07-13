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