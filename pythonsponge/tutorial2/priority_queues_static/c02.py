MAXSIZE = 5

qItems = [None] * MAXSIZE
qPriorities = [None] * MAXSIZE

front = 0
rear = -1
size = 0

def doInsert(item, priority):
  if size == MAXSIZE:
    raise Exception("queue has run out of space!")
  ptr = (rear + 1) % MAXSIZE
  while ptr != front and qPriorities[(ptr-1) % ________] < priority:
    qItems[ptr] = qItems[______________]
    qPriorities[ptr] = qPriorities[______________]
    ptr = (ptr-1) % ________
  qItems[ptr] = item
  qPriorities[ptr] = priority  

while True:
  choice = input("choose 1) enqueue, 2) dequeue 3) quit: ")
  if choice == "3":
    break
  elif choice == "1":
    newItem = input("enter item to add: ")
    newPriority = int(input("enter priority, higher better: "))
    doInsert(newItem, newPriority)
    rear += 1
    size += 1
    print(qItems)
  elif choice == "2":
    if front > rear:
      print("nothing to deqeue")
    else:
      print(qItems[front], "removed")
      qItems[front] = None
      front = (front + 1) % ________
      size -= __
      print(qItems)

print("goodbye!")
