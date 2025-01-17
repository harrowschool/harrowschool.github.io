initial = int(input())
previous = initial

while True:
    current = int(input())
    if current < previous:
      break
    previous = current

print(current - initial)