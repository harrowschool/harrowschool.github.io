num = float(input("enter a decimal number: "))

while True:
    decimalPlaces = int(input("enter the number of decimal places to round to or -1 to finish: "))
    if decimalPlaces == -1:
        break
    print(f"rounding {num} to {decimalPlaces}dp gives {num:.{decimalPlaces}f}")