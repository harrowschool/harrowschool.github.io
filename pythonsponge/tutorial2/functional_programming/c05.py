from functools import reduce


def add_one(num):
    return num + 1


def concatenate(a, b):
    return a + b


def add_to_list(lst, value):
    return lst + [value]


nums = [2, 3, 5, 7, 11, 13]
nums = list(___(add_one, ___))
strings = map(___, ___)
concatenated = ___(___, ___)
print(concatenated)

nums = reduce(___, ___, ___)
print(nums)
