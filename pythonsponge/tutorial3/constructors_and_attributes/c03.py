from dataclasses import dataclass


class Car:

  def __init__(self, cylinders):
    # The engine is created within the car and is only supposed to be used by the car.
    # The code does not use any instances of the class Engine other than those which are the children of a Car.
    # Thus we have composition
    self.engine = Engine(cylinders)

    # Person objects are independently created outside of Car and are only sometimes used by Car.
    # References to people are passed into the car, but the car does not create them or 'own' them.
    # Thus we have aggregation
    self.driver = None

  def drive(self, driver):
    self.driver = driver
    print(self.driver.name + " revs the engine")
    self.engine.rev()


@dataclass
class Engine:
  cylinders: int

  def rev(self):
    print("vroom " * self.cylinders)


@dataclass
class Person:
  name: str
  age: int
  children: list['Person']
  ...


# Person has a separate existence, with an instance being assigned to its own variable
docBrown = Person("Doc Brown", 65, [])
delorean = Car(6)
delorean.drive(docBrown)
