import time

num = int(input("enter a number for me to count up to: "))

print("ok, here I go, press ctrl-c if you want to quit me!")

for count in range(1, num + 1):
  time.sleep(1)
  print(count)