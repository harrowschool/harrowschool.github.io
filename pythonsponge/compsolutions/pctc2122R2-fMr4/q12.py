caves = input()
perm = int(input())

# only 1 option if on either of the last 2 letters
fib = [1, 1]

# work backwards to number of options from first cave
while len(fib) < len(caves):
    fib.insert(0, fib[0] + fib[1])

# start on cave 0
pos = [0]

while pos[-1] != len(caves) - 1:
    if fib[pos[-1] + 1] >= perm:
        pos.append(pos[-1] + 1)
    else:
        perm -= fib[pos[-1] + 1] 
        pos.append(pos[-1] + 2)

# convert cave positions to letters
print("".join(map(lambda p: caves[p], pos)))