num = float(input("enter a decimal: "))
choice = int(input("enter a rounding choice 0, 1 or 2: "))
if choice == 0:
  print(f"{num:.0f}")
elif choice == 1:
  print(f"{num.1f}")
elif choice == 2:
  print("{num:.2f}")
else:
  print("invalid choice")