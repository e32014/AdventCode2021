from copy import deepcopy

file = open("input.txt")

fishes = [int(val) for val in file.readline().strip().split(",")]
periods = [0] * 9
for fish in fishes:
    periods[fish] = periods[fish] + 1
fishCount = len(fishes)
days = 256
weeks = days // 7
additional = days % 7
for _ in range(weeks):
    nextWeek = [0] * 9
    sevens = periods[7]
    eights = periods[8]
    periods[7] = 0
    periods[8] = 0
    for i in range(len(periods)):
        nextWeek[(i + 2) % 9] = periods[(i + 2) % 9] + periods[i]
    nextWeek[0] = nextWeek[0] + sevens
    nextWeek[1] = nextWeek[1] + eights
    periods = deepcopy(nextWeek)

addon = 0
for i in range(additional):
    addon += periods[i]

print(sum(periods) + addon)