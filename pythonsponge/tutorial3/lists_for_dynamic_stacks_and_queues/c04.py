class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._items.pop()
    
    def is_empty(self):
        return self._items == []
    
    def peek(self):
        return self._items[-1]
    
class Queue:
    def __init__(self):
        self._items = []

    # ==> complete the two essential queue methods

    def enqueue(self, item):
        self._items.__________________

    def dequeue(self):
        if self.____________:
            raise Exception("Queue is empty")
        return self.____________
    
    def is_empty(self):
        return self._items == []
    
    def size(self):
        return len(self._items)
    
my_queue = Queue()
my_queue.enqueue("dog")
my_queue.enqueue("cat")
my_queue.enqueue("bat")
my_queue.enqueue("rat")
my_queue.enqueue("elephant")
my_queue.enqueue(input("enter an animal to add: "))

my_stack = Stack()
while not my_queue.is_empty():
    my_stack.push(my_queue.dequeue())

# ==> complete the following to add the items back to the queue
while not my_stack.is_empty():
    my_queue._____(my_stack._____)

print("Final queue order:")
while not my_queue.is_empty():
    print(my_queue.dequeue())