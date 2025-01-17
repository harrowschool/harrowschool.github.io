def print2D(lst):
    for row in lst:
        for element in row:
            print(element, end=" ")
        print()
    print()

# 2D list of integers
my2DList = [[0 for _ in range(5)] for _ in range(5)]
my2DList[2][2] = 1
print2D(my2DList)

# Alternative syntax
my2DList = [[0] * 5 for _ in range(5)]
my2DList[2][2] = 1
print2D(my2DList)

# But note that the * technique can only be used for lists of immutable types (e.g. integers)
# Note how this approach goes wrong!
my2DList = [[0] * 5] * 5
my2DList[2][2] = 1
print2D(my2DList)
# my2DList now consists of only one list, repeated 5 times
