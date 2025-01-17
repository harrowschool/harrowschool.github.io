# Hash Table Class
class HashTable:

    def __init__(self, size): # Constructor
        
        self.__size = size # Save the size
        self.__array = [None]*size # Create underlying array (using python list)
    

    @property
    def size(self):
        return self.__size
    

    '''Hash Function'''
    def __hash(self, key : str): # Simple hash function (that isn't very good!)
        return sum([ord(i) for i in key]) % self.__size # Sum up ASCII values for each character and mod by size of hash table
    
    
    '''Lookup with Open Addressing Collision Handling'''
    def lookup(self, key : str): # Lookup method, returns item if found, otherwise raises an error

        address = self.__hash(key) # Calculate address

        if (item := self.__array[address]) is not None:

            if key == item[0]: # No collision occured when storing this item
                return item[1]
            
            # Open Addressing Collision Handling Technique
            curr = address
            checked = 0
            while self.__array[curr] is None or self.__array[curr][0] != key: # While slot is empty or slot's key doesn't match our desired key
                curr = (curr + 1) % self.__size # Increment address with wraparound
                checked += 1
                if checked == self.__size:
                    break
            
            if checked == self.__size: # If we checked all possible addresses
                raise Exception(f"{key} is not in the hash table") # Item not found

            return self.__array[curr][1] # Found it, return the value
        
        raise Exception(f"{key} is not in the hash table")
    

    '''Insert with Open Addressing Collision Handling'''
    def insert(self, key : str, value): # Insert method

        address = self.__hash(key) # Calculate address

        if self.__array[address] is None: # Empty slot (no collision)
            self.__array[address] = (key, value) # we store both key and address for open addressing to work

        else: # Collision occurred

            # Open Addressing Collision Handling Technique
            curr = address
            checked = 0
            while self.__array[curr] is not None: # While slot is not empty
                curr = (curr + 1) % self.__size # Increment address with wraparound
                checked += 1
                if checked == self.__size:
                    break
            
            if checked == self.__size: # If we checked all possible addresses
                raise Exception("Hash table is full, please rehash") # Hash table is full, no empty slot to insert into

            self.__array[curr] = (key, value) # Found an empty space, store the key and value
            print(f"Collision occured when inserting ({key}, {value}), handled with open addressing")
    
    
    '''Rehashing'''
    def rehash(self):

        # Create new hash table
        new_hash_table = HashTable(self.__size * 2)

        # Loop through all items, and insert them into the new hash table
        for item in self.__array:
            if item is not None:
                new_hash_table.insert(item[0], item[1])

        # Change instance of current hash table to instance of new hash table
        self.__dict__ = new_hash_table.__dict__


    def __repr__(self): # Method to show array when object is printed
        return str(self.__array)
    



my_hash_table = HashTable(20) # Create new hash table

'''Items to insert, notice that pairs of keys are anagrams of each other, 
so when the hash function is applied, they return the same address'''

items_to_insert = [("petal", 56), ("plate", 93), 
                   ("horse", 14), ("shore", 38), 
                   ("rinse", 87), ("siren", 64)]

for key, value in items_to_insert: # Insert items
    my_hash_table.insert(key, value)

'''Notice that when a collision occurs, with open addressing, 
the item is stored at the next empty slot'''
print(my_hash_table) # Just to show what the hash table's array looks like

for key, _ in items_to_insert: # Lookup values
    print(my_hash_table.lookup(key), end=" ")
print("\n")

# Rehashing
print(my_hash_table.size)
my_hash_table.rehash()

print(my_hash_table)
print(my_hash_table.size) # We double the size (20 -> 40)