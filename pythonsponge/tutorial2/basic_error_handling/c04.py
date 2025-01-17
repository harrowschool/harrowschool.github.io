result = a / b
except Exception as e:
print("an error occurred:")
b = float(input("enter number b: "))
try:
print(e)
print(f"dividing a by b gives {result:.2f} rounded to 2dp")
a = float(input("enter number a: "))