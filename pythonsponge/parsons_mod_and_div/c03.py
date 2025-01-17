hour = int(input("enter start hour 1-12: "))
hour += int(input("enter hours to add: "))
hour = (hour - 1) % 12
hour += 1 
print(f"now it is {hour} o'clock")