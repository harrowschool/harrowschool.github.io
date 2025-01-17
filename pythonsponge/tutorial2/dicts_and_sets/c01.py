from datetime import datetime

iterations = int(input("Enter a number of iterations to run: "))

# With lists
start = datetime.now()
nums = [0]
if iterations < 10:
    print(f"List after 1 iteration: {nums}")

for i in range(1, iterations):
    # Three basic operations: append, check membership, remove
    nums.append(i)
    if i//2 in nums:
        nums.remove(i // 2)

    if iterations < 10:
        print(f"List after {i+1} iterations: {nums}")

print(f"{iterations} iterations on a list took time {datetime.now() - start}")

# With sets
start = datetime.now()
nums = {0}
if iterations < 10:
    print(f"Set after 1 iteration: {nums}")

for i in range(1, iterations):
    # Three basic operations: add, check membership, remove
    nums.add(i)
    if i//2 in nums:
        nums.remove(i // 2)

    if iterations < 10:
        print(f"Set after {i+1} iterations: {nums}")

print(f"{iterations} iterations on a set took time {datetime.now() - start}")
