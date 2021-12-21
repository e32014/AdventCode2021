import functools
import re
from copy import deepcopy


@functools.lru_cache(maxsize=None)
def multidimensionalHell(pos1, pos2, score1, score2, rolled, roll_count, turn):
    if score1 >= 21:
        return [1, 0]
    elif score2 >= 21:
        return [0, 1]
    totalWins = [0, 0]
    if roll_count == 3:
        if turn == 0:
            updatedpos = (pos1 + rolled) % 10
            updatedscore = score1 + updatedpos + 1
            wins1, wins2 = multidimensionalHell(updatedpos, pos2, updatedscore, score2, 0, 0, (turn + 1) % 2)
        else:
            updatedpos = (pos2 + rolled) % 10
            updatedscore = score2 + updatedpos + 1
            wins1, wins2 = multidimensionalHell(pos1, updatedpos, score1, updatedscore, 0, 0, (turn + 1) % 2)
        totalWins[0] += wins1
        totalWins[1] += wins2
    else:
        for i in range(1, 4):
            wins1, wins2 = multidimensionalHell(pos1, pos2, score1, score2, rolled + i, roll_count + 1, turn)
            totalWins[0] += wins1
            totalWins[1] += wins2
    return totalWins


file = open('input.txt')

pos = []
score = []
die = 0
rolls = 0
for line in file:
    player, start = re.match('Player ([0-9]+) starting position: ([0-9]+)', line.strip()).groups()
    pos.append(int(start) - 1)
    score.append(0)

print(pos, score)
# turn = 0
# while not any([val >= 1000 for val in score]):
#    move = 0
#    for _ in range(3):
#        move += die + 1
#        rolls += 1
#        die = (die + 1) % 100
#    pos[turn] = (pos[turn] + move) % 10
#    score[turn] += pos[turn] + 1
#    turn = (turn + 1) % 2
# print(min(score) * rolls)

print(max(multidimensionalHell(pos[0], pos[1], score[0], score[1], 0, 0, 0)))