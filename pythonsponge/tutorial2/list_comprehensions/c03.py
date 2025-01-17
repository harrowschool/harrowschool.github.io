# produce a 2D list of integers using list comprehensions
grid = [[col + row for col in range(6)] for row in range(4)]
print(grid)

# now flatten it into a 1D list filtering to only include even numbers
flat_filtered = [num for row in grid for num in row if num % 2 == 0]
print(flat_filtered)

