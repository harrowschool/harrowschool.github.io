from functools import partial


def exponentiate(base, exponent):
    return base ** exponent


power_of_two = partial(exponentiate, 2)
print("Two to the ten is", power_of_two(10))

cube = partial(exponentiate, exponent=3)
print("Eleven cubed is", cube(11))
