class LinkedListNode:

    def __init__(self, value, next):
        self.value = value
        self.next = next
    
    def __repr__(self):
        return f"{self.value}/{self.next}"


class HashTable:

    def __init__(self, size):
        self.__size = _______
        self.__array = [None]*_______

    
    '''Hash Function'''
    def __hash(self, key : str):
        return sum([ord(i) for i in key]) % self.__size
    
    
    '''Lookup with Chaining Collision Handling'''
    def lookup(self, key : str):

        address = self.__hash(key) # Calculate address

        if (item := self.__array[address]) is not None:

            if type(item) == tuple and _______ == item[0]: # No collision occurred
                return _______[1]
            
            # Chaining Collision Handling Technique
            curr = ______
            while curr.next is not None and curr.value[0] != key:
                curr = curr.______
            
            if curr.value[0] == key:
                return curr.______[1] # Found it, return the value
        
            raise Exception(f"{key} is not in the hash table")
        
        raise Exception(f"{key} is not in the hash table")
    

    '''Insert with Chaining Collision Handling'''
    def insert(self, key : str, value): # Insert method

        address = self.__hash(key) # Calculate address

        if self.__array[address] is None: # Empty slot (no collision)
            self.__array[address] = (key, value) # we store both key and address for open addressing to work
        
        else: # Collision occurred, handle with chaining technique

            if type(self.__array[address]) == tuple: # If linked list not yet created
                node = self.__array[_________]
                self._________[address] = LinkedListNode(node, None) # Create the head of the linked list
            
            nextnode = LinkedListNode((key, value), None)
            curr = self.__array[address]
            while curr._______ is not None:
                curr = curr.______
            curr.next = _______________ # Add the next node on
            
            
    def __repr__(self): # Method to show array when object is printed
        return str(self.__array)
    



my_hash_table = HashTable(20) # Create new hash table

'''Items to insert, notice that triplets of keys are anagrams of each other, 
so when the hash function is applied, they return the same address'''

items_to_insert = [("petal", 56), ("plate", 93), ("leapt", 71), 
                   ("horse", 14), ("shore", 38), ("hoser", 25),
                   ("bustle", 87), ("subtle", 64), ("sublet", 37)]

for key, value in items_to_insert: # Insert items
    my_hash_table.insert(key, ________)

'''Notice that when a collision occurs, with open addressing, 
the item is stored at the next empty slot'''
print(my_hash_table) # Just to show what the hash table's array looks like

for key, _ in items_to_insert: # Lookup values
    print(my_hash_table.lookup(_______), end=" ")