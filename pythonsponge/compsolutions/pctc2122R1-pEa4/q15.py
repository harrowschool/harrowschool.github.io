weather = input()
lap = int(input())

distance = 2 * lap

if weather == "warm" and distance <= 10:
  distance += lap

print(distance)