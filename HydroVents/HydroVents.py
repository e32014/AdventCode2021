import re

file = open("input.txt")

grid = dict()

for line in file:
    x1, y1, x2, y2 = [int(val) for val in re.match("([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)", line.strip()).groups()]
    if x1 != x2 and y1 != y2:
        slope = int((y1 - y2) / (x1 - x2))
        start, end = [x1, x2] if x1 < x2 else [x2, x1]
        ypos = y1 if x1 < x2 else y2
        for i in range(start, end + 1):
            grid[(i, ypos)] = grid.setdefault((i, ypos), 0) + 1
            ypos += slope
    elif x1 == x2:
        for i in range(min(y1, y2), max(y1, y2)+1):
            grid[(x1, i)] = grid.setdefault((x1, i), 0) + 1
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            grid[(i, y1)] = grid.setdefault((i, y1), 0) + 1

print(grid)
print(len([key for key in grid.keys() if grid[key] > 1]))