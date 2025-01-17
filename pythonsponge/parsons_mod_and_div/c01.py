hour = int(input("enter start hour 0-11: "))
hour += int(input("how many hours to add?"))
hour = hour % 12
print(hour)