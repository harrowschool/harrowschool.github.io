h0 = 0
h1 = 0

field0 = "H"
field1 = "H"

while h0 < 11 and h1 < 11:
    if int(input()):
        h1 += 1
        field1 = "." + field1
    else:
        h0 += 1
        field0 = "." + field0

if field0[0] == ".":
    field0 = "|" + field0[1:]

if field1[0] == ".":
    field1 = "|" + field1[1:]

while len(field0) < 11:
    field0 += "."

while len(field1) < 11:
    field1 += "."

if len(field0) != 12:
    field0 += "|"

if len(field1) != 12:
    field1 += "|"

print(field0)
print(field1)


# consider also

'''
def track(horse):
    field = ""
    for pos in range(12):
        if pos == horse:
            field += 'H'
        elif pos in [0, 11]:
            field += '|'
        else:
            field += '.'
    return field


first = 0
second = 0

while first < 11 and second < 11:
    if input() == '0':
        first += 1
    else:
        second += 1

print(track(first))
print(track(second))
'''
