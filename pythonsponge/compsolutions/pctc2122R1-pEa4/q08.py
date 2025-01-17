num_readings = int(input())
alt = int(input())

ascent = 0
descent = 0

for _ in range(num_readings):
  new_alt = int(input())
  if new_alt > alt:
    ascent += (new_alt - alt)
  else:
    descent += (alt - new_alt)
  alt = new_alt
  
print(ascent)
print(descent)