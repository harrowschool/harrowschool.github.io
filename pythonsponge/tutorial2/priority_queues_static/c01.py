# A STATIC PRIORITY (NON-CIRCULAR) QUEUE

MAXSIZE = 5

qItems = [None] * MAXSIZE
qPriorities = [None] * MAXSIZE

front = 0
rear = -1

def doInsert(item, priority):
  if rear == MAXSIZE - 1:
    raise Exception("queue has run out of space although annoyingly there may be empty spaces at the start!")
  ptr = rear + 1
  while ptr > front and qPriorities[ptr-1] < priority:
    qItems[ptr] = qItems[ptr-1]
    qPriorities[ptr] = qPriorities[ptr-1]
    ptr -= 1
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
    print(qItems)
  elif choice == "2":
    if front > rear:
      print("nothing to deqeue")
    else:
      print(qItems[front], "removed")
      qItems[front] = None
      front += 1
      print(qItems)

print("goodbye!")
