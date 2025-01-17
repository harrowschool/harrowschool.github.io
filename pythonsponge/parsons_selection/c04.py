speed = int(input("enter your speed: "))
if speed > 70:
    print("speeding ... slow down!")
elif speed >= 40:
    print("acceptable speed ... continue carefully!")
else:
    print("this road has a minimum speed limit ... please speed up!")