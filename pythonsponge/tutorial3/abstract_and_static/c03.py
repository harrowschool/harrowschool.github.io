from abc import ABC, abstractmethod
from functools import partial


class Skins:
  '''Class to store player skins and demonstrate static attributes'''

  # Static attributes
  SKIN0 = "(^ω^)"
  SKIN1 = "(●´ω｀●)"
  SKIN2 = "ᕦ(ò_óˇ)ᕤ"

  @staticmethod
  def get_skin_names():  # STATIC METHOD to get all skin names
    return [attr for attr in dir(Skins) if not callable(getattr(Skins, attr)) and not attr.startswith("__")]

  @staticmethod
  def get_skin_values():  # STATIC METHOD to get all skin values - lookup partial if interested!
    return list(map(partial(getattr, Skins), Skins.get_skin_names()))


class Player(ABC):
  '''Player class (abstract class)'''

  def __init__(self):  # Constructor
    super().__init__()
    self._skin = Skins.SKIN0
    self._position = [0, 0]

  def upgrade_skin(self, skin):
    self._skin = skin

  @property
  def position(self):
    return self._position

  @abstractmethod
  def attack(self):
    pass

  def move(self):
    self._position[0] += 1
    self._position[1] += 1

  def __repr__(self):  # Printing method
    return f"{self._skin} is at position {self._position}"


class Warrior(Player):
  '''Warrior class inherits from Player class'''

  def __init__(self):  # Constructor
    super().__init__()

  def move(self):  # Override virtual method
    self._position[0] += 2
    self._position[1] += 2

  def attack(self):  # Override the abstract method
    print("Warrior is attacking with a sword.")


class Mage(Player):
  '''Mage class inherits from Player class'''

  def __init__(self):  # Constructor
    super().__init__()

  def move(self):  # Override virtual method
    self._position[0] += 0.5
    self._position[1] += 0.5

  def attack(self):  # Override the abstract method
    print("Mage is casting a fireball.")


# Create instances of the classes
warrior = Warrior()
mage = Mage()

# Change skins
warrior.upgrade_skin(Skins.SKIN1)  # Access static attributes to set skin
mage.upgrade_skin(Skins.SKIN2)  # Access static attributes to set skin

# Show skins and positions of warrior and mage
print(warrior)
print(mage)

# See all available skins
print("Available skins are:", Skins.get_skin_names())
print("... which have values:", Skins.get_skin_values())
