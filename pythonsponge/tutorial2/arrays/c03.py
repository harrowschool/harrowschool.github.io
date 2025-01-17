from time import time

# first using append
myList = []

start = time()
for i in range(100000):
    myList.append(i)

end = time()
print(f"Time taken to append 100,000 items to a list: {end - start}")

# second using insert (at the start)
myList = []

start = time()
for i in range(100000):
    myList.insert(0, i)

end = time()
print(f"Time taken to insert 100,000 items at the start of a list: {end - start}")
