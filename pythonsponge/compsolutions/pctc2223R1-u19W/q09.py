x = int(input())
y = int(input())

for row in range(10):
    output = ""
    for col in range(10):
        if row == y and col == x:
            output += "X"
        else:
            output += "#"
    print(output)

# consider also

'''
x, y = int(input()), int(input())

for i in range(10):
    for j in range(10):
        if i == y and j == x:
            print('X', end='')
        else:
            print('#', end='')
    print()
'''