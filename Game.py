dice = [1, 2, 3, 4, 5, 6]

roll_2 = []
for i in dice:
    for j in dice:
        roll_2.append(i + j)

all_rolls = []
for x in roll_2:
    for xx in roll_2:
        for xxx in roll_2:
            all_rolls.append([x, xx, xxx])

print("total possiblities: ", len(all_rolls))


def rule(num):
    if num <= 3:
        return 10
    elif num == 4:
        return -10
    elif num == 5:
        return 5
    elif num == 6 or num == 7:
        return -5
    elif num == 8 or num == 9:
        return 15
    elif num >= 10:
        return 10


winner = 0
for r in all_rolls:
    score = 0
    for i in range(0, 3):
        if score < 45:
            score += rule(r[i])
    if score >= 45:
        winner += 1

print("total winners: ", winner)
