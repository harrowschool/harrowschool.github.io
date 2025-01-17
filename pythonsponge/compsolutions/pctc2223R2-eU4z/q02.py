firstname1, age1 = input().split()
firstname2, age2 = input().split()
diff = int(age1) - int(age2)

if diff > 0:
    print(f"NOT TWINS:{firstname1} is {abs(diff)} year(s) older than {firstname2}")
elif diff < 0:
    print(f"NOT TWINS:{firstname1} is {abs(diff)} year(s) younger than {firstname2}")
else:
    print(f"MAYBE TWINS:{firstname1} and {firstname2} are the same age")

# ALSO CONSIDER

'''
firstname1, age1 = input().split()
firstname2, age2 = input().split()
diff = abs(int(age1) - int(age2))

TEMPLATES = (
    f"MAYBE TWINS:{firstname1} and {firstname2} are the same age",
    f"NOT TWINS:{firstname1} is {diff} year(s) older than {firstname2}",
    f"NOT TWINS:{firstname1} is {diff} year(s) younger than {firstname2}"
)

cmp = lambda x, y: (x > y) - (x < y)

print(TEMPLATES[cmp(int(age1), int(age2))])

'''