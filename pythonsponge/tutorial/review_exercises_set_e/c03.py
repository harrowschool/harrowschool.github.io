BUY = 96
SELL = 128

MESSAGE = "Converting {_} British pounds will give {1} Indian rupees " + \
"but converting {1} rupees back at the end of the holiday " + \
"would only give {_} pounds because we have different BUY/SELL rates"

amount = int(input("enter number of pounds to convert: "))
result = MESSAGE.format(______, amount * BUY, amount * BUY // SELL)

print(result)

 