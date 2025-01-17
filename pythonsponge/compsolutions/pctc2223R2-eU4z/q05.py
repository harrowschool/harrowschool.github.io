lastWand = -1
scores = [0,0]

for _ in range(6):
    game = input()
    if game == "WW":
        if lastWand >= 0:
            scores[lastWand] = 0
    elif game[0] == "W":
        scores[0] += 1
        lastWand = 0
    elif game[1] == "W":
        scores[1] += 1
        lastWand = 1
    elif game in ["SP", "PR", "RS"]:
        scores[0] += 1
    elif game in ["PS", "RP", "SR"]:
        scores[1] += 1

print(f"{scores[0]}-{scores[1]}")