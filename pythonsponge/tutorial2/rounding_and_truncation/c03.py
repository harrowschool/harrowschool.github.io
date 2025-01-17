num1 = 1.5
num2 = 2.5

num1Rounded = round(num1, 1)
num2Rounded = round(num2, 1)

print(f"rounding {num1} to 1dp gives {num1Rounded}")
print(f"rounding {num2} to 1dp gives {num2Rounded}")

num1 = 0.1
num2 = 0.2
num3 = 0.3

print(f"evaluating whether {num1} + {num2} > {num3}")
result = ((num1 + num2) > num3)
print("result:", result)