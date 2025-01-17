from dataclasses import dataclass


# Dataclass with separate function for behaviour
@dataclass
class Person:
  forename: str
  surname: str
  children: 'list[Person]'


# Note there is no obvious link to the Person class until you read the function body
def create_child(parent, forename):
  parent.children.append(Person(forename, parent.surname, []))


# We customarily use a capital letter for a class name and a lowercase letter for a regular object
henry = Person("Henry", "Tudor", [])
# Potentially confusing syntax
create_child(henry, "Mary")
create_child(henry, "Elizabeth")
create_child(henry, "Edward")


# Alternative Dataclass showing a contained function for behaviour
@dataclass
class Person:
  forename: str
  surname: str
  children: 'list[Person]'

  # Function is defined in class body so clearly related. We call such a function a method.
  # The first parameter is customarily called self, as it refers to the object from which the method is called, which
  # in a sense "owns" the method
  def create_child(self, forename):
    self.children.append(Person(forename, self.surname, []))


henry = Person("Henry", "Tudor", [])
# Access the function as a property of the class with a dot.
Person.create_child(henry, "Mary")

# But here is a more convenient syntax. Here we need not even refer to Person directly,
# only to its instance henry which is implictly passed as the first argument of the method
# and so becomes the value of the self parameter.
# This is the usual syntax for invoking methods.
henry.create_child("Elizabeth")
henry.create_child("Edward")

print(henry)
