w = input()
rev = w[3] + w[2] + w[1] + w[0]

# also consider:
# rev = w[::-1]

if w < rev:
    print(w)
    print(rev)
else:
    print(rev)
    print(w)