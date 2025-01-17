class Person:
  '''Person class as a base class'''

  def __init__(self, name, age):
    self._age = ______  # age (protected)
    self._name = ______  # private (protected)

  '''GETTERS'''

  def get_age(self):  # Getter for age
    return ________

  def get_name(self):  # Getter for name
    return _______

  '''SETTERS'''

  def set_age(self, age):  # Setter for age with validation
    if age >= 0:
      _______ = age
    else:
      raise ValueError("Age cannot be negative")

  def set_name(self, name):  # Setter for name with validation
    if len(name) > 0 and name.isalpha():
      ________ = name
    else:
      raise ValueError(
          "Name cannot be empty or contain non-alphabetic characters")


class Employee(Person):
  '''Employee class inherits from Person class'''

  def __init__(self, name, age, employee_id):
    super().__init__(name, age)  # Call the parent class constructor
    self.__employee_id = _________  # Additional private attribute for Employee

  def get_employee_id(self):
    return _____________

  def set_employee_id(self, employee_id):
    try:
      employee_id = int(employee_id)
      if employee_id >= 0:
        _____________ = employee_id
      else:
        raise ValueError("Employee ID cannot be negative")
    except ValueError:
      raise ValueError("Employee ID must be an integer")


employee = Employee("John", 25, 1234)

# get attributes
print(employee.________(), employee.get_name(), employee.get_employee_id())

employee.set_age(30)  # set age
employee.set_name("Mike")  # set name
employee.____________(5678)  # set employee id

# get attributes
print(employee.get_age(), employee.________(), employee.get_employee_id())
