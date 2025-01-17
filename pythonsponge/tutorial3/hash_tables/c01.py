# Hash Table Class
class HashTable:

  def __init__(self, size):  # Constructor

    self.__size = size  # Save the size
    self.__array = [None]*size  # Create underlying array (using python list)

  '''Hash Function'''

  def __hash(self, key: str):  # Simple hash function for demonstration (that isn't very good!)
    # Sum up ASCII values for each character and mod by size of hash table
    return sum([ord(i) for i in key]) % self.__size

  '''Lookup'''

  def lookup(self, key: str):  # Lookup method, returns item if found, otherwise raises an error
    address = self.__hash(key)
    if (item := self.__array[address]) is not None:
      return item
    raise Exception(f"{key} is not in the hash table")

  '''Insert'''

  def insert(self, key: str, value):  # Insert method (needs to be modified to handle collisions!!!)
    address = self.__hash(key)
    self.__array[address] = value

  def __repr__(self):  # Method to show array when object is printed
    return str(self.__array)


my_hash_table = HashTable(100)  # Create new hash table

try:

  for key, value in [("Apple", 1), ("Orange", 2), ("Banana", 5), ("Grape", 3), ("Watermelon", 10)]:
    my_hash_table.insert(key, value)

  print(my_hash_table)  # Just to show what the hash table's array looks like

  print(my_hash_table.lookup("Watermelon"))  # This should work fine
  # This should throw an error as "Peach" is not in the hash table
  print(my_hash_table.lookup("Peach"))

except Exception as err:  # Catch errors
  print(err)
