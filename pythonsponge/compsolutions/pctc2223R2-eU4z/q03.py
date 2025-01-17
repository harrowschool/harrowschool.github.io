n = int(input())
print("___")
for i in range(n):
    print(f"###{'##' * i}]_{('','__')[i==n-1]}")