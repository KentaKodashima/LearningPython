# For this challenge, create a bank account class that has two attributes:
# owner
# balance

# and two methods:
# deposit
# withdraw

# As an added requirement, withdrawals may not exceed the available balance.

# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
  def __init__(self,owner,balance):
    self.owner = owner
    self.balance = balance
  
  def deposit(self,amount):
    self.balance += amount
    print('Deposit Accepted')

  def withdraw(self,amount):
    if (self.balance < amount):
      print('Funds Unavailable!')
    self.balance -= amount
    print('Withdrawal Accepted')

# 1. Instantiate the class
acct1 = Account('Jose',100)

# 2. Print the object
# Account owner:   Jose
# Account balance: $100
print(acct1)

# 3. Show the account owner attribute
print(acct1.owner) #'Jose'

# 4. Show the account balance attribute
print(acct1.balance) # 100

# 5. Make a series of deposits and withdrawals
acct1.deposit(50) # Deposit Accepted

acct1.withdraw(75) # Withdrawal Accepted

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500) # Funds Unavailable!