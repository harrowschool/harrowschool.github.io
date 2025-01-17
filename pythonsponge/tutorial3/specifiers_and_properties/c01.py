class BankAccount:
  '''Class for bank account'''

  def __init__(self, account_number, balance=0):  # Constructor
    self.__account_number = account_number  # private attribute
    self.__balance = balance  # private attribute

  '''Getters'''

  def get_account_number(self):  # Getter for account number
    return self.__account_number

  def get_balance(self):  # Getter for balance
    return self.__balance

  '''Setters'''

  def deposit(self, amount):  # Deposit money (add to balance)
    self.__balance += amount

  def withdraw(self, amount):  # Withdraw money (subtract from balance)
    if self.__balance >= amount:
      self.__balance -= amount
    else:
      print("Insufficient funds")

  # Method used to show specific message whenever the class object is printed.
  # If this is not included, printing the class will show <__main__.BankAccount object at some address>
  def __repr__(self):
    return f"Account Number: {self.__account_number}\nBalance: {self.__balance}"


# Creating an instance of BankAccount
account = BankAccount("012345678", 1000)

# Attempting to access private attribute
try:
  print("this next line should trigger an error since direct access is not allowed ...")
  print(account.__account_number)
except Exception as err:
  print(f"Error caught: {err}")

# Read-only access via getters
print(account.get_account_number())
print(account.get_balance())

account.deposit(200)  # deposit 200

# WHENEVER you call print(object), the string returned from __repr__ is printed
print(account)  # print details
account.withdraw(100)  # withdraw 100
print(account)  # print details
account.withdraw(1500)  # try to withdraw 1500
print(account)  # print details
