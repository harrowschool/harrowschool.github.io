from datetime import date
from dataclasses import dataclass

# Original shows less readable and maintainable code

myCar = {
    "make": "DeLorean",
    "model": "DMC-12",
    "colour": "grey",
    "registration": "OUTATIME",
    "lastService": date(1995, 10, 21)
}


def print_car(car):
  print(f"{car['colour']} {car['make']} model {car['model']} with registration plate {car['registration']}")
  print(f"Last serviced on {car['lastService']}")


def service(car):
  car["lastService"] = date.today()


def re_register(car, registration):
  car['registration'] = registration


print_car(myCar)
service(myCar)
re_register(myCar, "FLUXCPCTR")
print_car(myCar)


# Fill in the blanks to rewrite the above using oop (leave the original intact)

@dataclass
class Car:
  make: str
  model: ___
  ___
  ___
  lastService: date

  def print_car(self):
    print(f"{self.___} {___} model {___} with registration plate {___}")
    print(f"Last serviced on {___}")

  def service(___):
    _____ = date.today()

  def re_register(___, ___):
    self.___ = ___


# Create a car with the same parameters as in the original
myCar = _____

# Do the same things here as on lines 27-30, but use method calls with a dot rather than calling the separate functions
myCar.print_car()
___
___
___
