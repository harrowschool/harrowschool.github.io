class Dog:

  def __init__(self):
    pass

  def make_sound(self):
    print("Woof!")


class Cat:

  def __init__(self):
    pass

  def make_sound(self):
    print("Meow!")


class Bulldog(Dog):
  '''Bulldog class, inherits from Dog'''

  def __init__(self):
    super().__init__()

  def make_sound(self):  # OVERRIDING: Override method inherited from Dog
    print("Woof! I'm a Bulldog!")


class PersianCat(Cat):
  '''Persian Cat class, inherits from Cat'''

  def __init__(self):
    super().__init__()

  def make_sound(self):  # OVERRIDING: Override method inherited from Cat
    print("Meow! I'm a Persian Cat!")


# Create instances of each class and add them to a list
my_pets = [Dog(), Cat(), Bulldog(), PersianCat()]

# RUN-TIME POLYMORPHISM: one method interface can be called for objects of different classes
for pet in my_pets:
  pet.make_sound()
