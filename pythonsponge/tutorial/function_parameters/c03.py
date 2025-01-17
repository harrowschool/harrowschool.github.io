def double_me(num):
  return num * 2

current = int(input("starting whole number: "))
repeat_count = int(input("double how many times: "))

for count in range(repeat_count):
  current = double_me(current)

print("result:", current)