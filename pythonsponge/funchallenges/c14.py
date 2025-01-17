class RangeError(Exception):
  pass

data = 'a'
while True:
  try:
    # Raises a type error for first input
    data -= 1
    # Raises an index error for the second input
    list = [1,2,3,4,5]
    x = list[data]
    # Raises a name error
    x = variable / data
    # Raises a zero division error
    x = data / variable
    # Raises a custom range error
    if data > variable:
      raise RangeError
    # Exit the loop
    break
    
  # Find out and fill in the relevant exception names 
  # the first one has been done for you...
  except TypeError:
    print("Expected integer data type...")
    data = 6
  except ______:
    print("Index out of range for list...")
    data = 5
  except ______:
    print("Variable 'variable' has not been assigned...")
    variable = 0
  except ______:
    print("Cannot divide by 0...")
    variable = 1
  except ______:
    print("Number is out of range...")
    data = -1