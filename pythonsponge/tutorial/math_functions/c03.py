import math

a = 177
b = 100

print("some people use {}/{} as an approximation to the square root of pi".format(a, b))

calc = math.sqrt(math.pi)

print("but a better approximation is", calc)

percent_error = (a/b - calc) / calc * 100

print("so the percentage error is {0:.2f}% to 2dp".format(percent_error))