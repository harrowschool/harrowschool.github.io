mySquares = [n ** 2 for n in range(10)]
print(mySquares)

def isPerfect(n):
    # a number is perfect if it is equal to the sum of its factors (excluding itself)
    return sum([i for i in range(1, n) if n % i == 0]) == n

myPerfectNumbers = [n for n in range(1, 1001) if isPerfect(n)]
print(myPerfectNumbers)
