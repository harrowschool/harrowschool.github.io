primes = [2, 3, 5, 7, 11, 13, 17, 19]

#start
primeStrings = []
for prime in primes:
    primeStrings.append(str(prime))
combined = ",".join(primeStrings)
print(combined)
