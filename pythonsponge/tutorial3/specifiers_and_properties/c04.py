class Pet:
  '''Pet class as a base class'''

  def __init__(self, name, age):
    self._age = ______  # age (protected)
    self._name = ______  # name (protected)

  '''GETTERS'''

  @property
  def age(self):  # Getter for age
    return ________

  @property
  def name(self):  # Getter for name
    return _______

  '''SETTERS'''

  @age.setter
  def age(self, value):  # Setter for age with validation
    if value >= 0:
      _______ = value
    else:
      raise ValueError("Age cannot be negative")

  @name.setter
  def name(self, value):  # Setter for name with validation
    if len(value) > 0 and value.isalpha():
      ________ = value
    else:
      raise ValueError(
          "Name cannot be empty or contain non-alphabetic characters")


class Dog(Pet):
  '''Dog class inherits from Pet class'''

  def __init__(self, name, age, microchip_id):
    super().__init__(name, age)  # Call the Pet class constructor
    self.__microchip_id = _________  # Additional attribute for Dog

  @___________
  def microchip_id(self):
    return _____________

  @___________.______
  def microchip_id(self, value):
    _____________ = value


my_dog = Dog("Panda", 7, "012345678901234")

# get attributes
print(my_dog.name, my_dog.___, my_dog.microchip_id)

my_dog.age += 1  # increase age
my_dog.name = "Pandu"  # change name
my_dog.microchip_id = "987654321098765"  # change microchip id

# get updated attributes
print(my_dog.name, my_dog.age, my_dog.____________)
