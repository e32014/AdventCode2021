file = open("input.txt")

depth = 0
aim = 0
distance = 0
for line in file:
    comms = line.strip().split(' ')
    if comms[0] == "forward":
        distance += int(comms[1])
        depth += aim * int(comms[1])
    elif comms[0] == "down":
        aim += int(comms[1])
    elif comms[0] == "up":
        aim -= int(comms[1])

print(depth * distance)