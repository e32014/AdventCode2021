from copy import deepcopy

file = open("input.txt")

fishes = [int(val) for val in file.readline().strip().split(",")]
today = [0] * 9
for fish in fishes:
    today[fish] = today[fish] + 1

days = 256
for _ in range(days):
    tomorrow = [0] * 9
    for i in range(7):
        tomorrow[i] = today[(i + 1) % 7]
    tomorrow[8] = today[0]
    tomorrow[7] = today[8]
    tomorrow[6] += today[7]
    today = deepcopy(tomorrow)

print(sum(today))