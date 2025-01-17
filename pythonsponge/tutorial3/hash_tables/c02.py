class HashTable:

    def __init__(self, size):
        
        self.__size = ______
        self.__array = [None]*____ 
    
    def __hash(self, key : str):
        return sum([(_______ + 1) * ord(_______) for index, char in _________(key)]) % ___________
    
    def lookup(self, key : str):
        address = self._________(key)
        if (item := self.__array[_________]) is not None:
            return ________
        raise Exception(f"{key} is not in the hash table")
    
    def insert(self, key : str, value):
        address = self.__hash(______)
        __________[address] = _________

    def __repr__(self):
        return str(self.__array)

my_hash_table = HashTable(20)

try:

    for key, value in [("Carrot", 4), ("Potato", 6), ("Tomato", 7), ("Cabbage", 3), ("Broccoli", 5)]:
        my_hash_table.________(key, _______)
    
    print(my_hash_table)
    
    print(my_hash_table.______("Tomato"))
    print(___________.lookup("Carrot"))
    print(my_hash_table.lookup("Lettuce"))

except Exception as err:
    print(err)