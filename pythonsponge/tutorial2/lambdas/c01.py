from functools import reduce

nums = [2, 3, 5, 7, 11, 13]
nums_plus_one = map(lambda num: num + 1, nums)
product = reduce(lambda a, b: a * b, nums_plus_one, 1)
print(product)
