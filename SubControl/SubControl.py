file = open("input.txt")

depth = 0
aim = 0
distance = 0
for line in file:
    command, dist = line.strip().split(' ')
    if command == "forward":
        distance += int(dist)
        depth += aim * int(dist)
    elif command == "down":
        aim += int(dist)
    elif command == "up":
        aim -= int(dist)

print(depth * distance)