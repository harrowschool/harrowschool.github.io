class BankAccount:
  '''Class for a bank account'''

  def __init__(self, account_number, balance=0):  # Constructor
    self.__account_number = account_number
    self.__balance = balance

  '''Getters'''

  @property
  def account_number(self):  # A read-only getter for account number with property decorator
    return self.__account_number

  @property
  def balance(self):  # A read-only getter for balance
    return self.__balance

  '''Setters'''

  @balance.setter
  def balance(self, amount):  # set new balance if amount is valid
    if amount >= 0:
      self.__balance = amount
    else:
      raise ValueError("Balance cannot be negative")

  # Method used to show specific message whenever the class object is printed.
  # If this is not included, printing the class will show <__main__.BankAccount object at some address>
  def __repr__(self):
    return f"Account Number: {self.__account_number}\nBalance: {self.__balance}"


# Creating an instance of BankAccount
account = BankAccount("012345678", 1000)

# Attempting to change account number attribute
try:
  print("this next line should trigger an error ...")
  account.account_number = "876543210"
except Exception as err:
  print(f"Error caught: {err}")

# Access via getter (NO brackets because @property is used)
print(account.account_number)
print(account.balance)  # Access via getter

account.balance = 200  # set balance to 200

# Attempting to set negative balance
try:
  print("this next line should trigger an error ...")
  account.balance = -100
except Exception as err:
  print(f"Error caught: {err}")

# WHENEVER you call print(object), the string returned from __repr__ is printed
print(account)  # print details still shows old balance
