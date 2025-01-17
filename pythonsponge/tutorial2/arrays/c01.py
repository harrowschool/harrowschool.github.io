# different ways of initialising a list to a given length in python
myIntegers = [0, 0, 0, 0, 0]
myStrings = [""] * 5
myDecimals = [0.0 for _ in range(5)]

print(myIntegers)
print(myStrings)
print(myDecimals)

print("but note that lists are not fixed length....")
myIntegers.append(1)
print(myIntegers)

print("...and these are not fixed type")
myIntegers.append("hello")
print(myIntegers)

print("so not formally arrays although we use them as such")

print("we can create arrays using ctypes if we really want to...")
import ctypes
myIntegersArr = (ctypes.c_int * 5)()
myIntegersArr[0] = 1
for idx in range(len(myIntegersArr)):
    print(myIntegersArr[idx], end=" ")

# TRY CHANGING LINE 23 to myArray[0] = "hello" and see what happens
# ALSO TRY CHANGING LINE 23 to myArray[10] = 1 and see what happens when out of bounds
# FINALLY TRY AN append OPERATION ON myIntegersArr and see what happens 