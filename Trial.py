import random

Dice = [1, 2, 3, 4, 5, 6]


def roll():
    return random.choice(Dice) + random.choice(Dice)


def rule(num):
    if num <= 3:
        return 10
    elif num == 4:
        return -10
    elif num == 5:
        x = roll()
        if x > 5:
            return 10 + rule(x)
        else:
            return 5 + rule(x)
    elif num == 6 or num == 7:
        return -5
    elif num == 8 or num == 9:
        return 15
    elif num >= 10:
        xx = roll()
        if xx == 10:
            return 20 + rule(xx)
        else:
            return 10 + rule(xx)


winner = 0
for test in range(0, 1000000):
    result = 0
    for rolls in range(0, 3):
        if result < 45:
            result += rule(roll())
    if result >= 45:
        winner += 1
    #print("test ", test, " has score ", result)

print(winner)
