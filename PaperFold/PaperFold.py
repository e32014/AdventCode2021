import re

file = open("input.txt")

grid = set()
line = file.readline().strip()
while line != "":
    grid.add(tuple([int(val) for val in line.split(",")]))
    line = file.readline().strip()

fold = file.readline().strip()
while fold != "":
    dir, pos = re.match('.*([xy])=([0-9]+)', fold).groups()
    pos = int(pos)
    remove = set()
    newPoints = set()
    for point in grid:
        if dir == 'x' and point[0] > pos:
            remove.add(point)
            newPoints.add((2*pos - point[0], point[1]))
        elif dir == 'y' and point[1] > pos:
            remove.add(point)
            newPoints.add((point[0], 2*pos - point[1]))
    grid = (grid - remove).union(newPoints)
    fold = file.readline().strip()

maxX = max([x for x,_ in grid]) + 1
maxY = max([y for _,y in grid]) + 1
dispGrid = [["."] * maxX for _ in range(maxY)]

for x, y in grid:
    dispGrid[y][x] = '#'
for row in dispGrid:
    print(row)