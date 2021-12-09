import functools
import operator

file = open("input.txt")

grid = []
for line in file:
    grid.append([int(val) for val in line.strip()])

lowPoints = []
basins = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if i - 1 > -1 and grid[i][j] >= grid[i - 1][j]:
            continue
        elif j - 1 > -1 and grid[i][j] >= grid[i][j - 1]:
            continue
        elif i + 1 < len(grid) and grid[i][j] >= grid[i + 1][j]:
            continue
        elif j + 1 < len(grid[i]) and grid[i][j] >= grid[i][j + 1]:
            continue
        lowPoints.append((i, j))

for lowPoint in lowPoints:
    visited = set()
    nextPoint = [lowPoint]
    while len(nextPoint) > 0:
        i, j = nextPoint.pop()
        visited.add((i, j))
        if i - 1 > -1 and (i - 1, j) not in visited and (i - 1, j) not in nextPoint and grid[i - 1][j] < 9:
            nextPoint.append((i - 1, j))
        if j - 1 > -1 and (i, j - 1) not in visited and (i, j - 1) not in nextPoint and grid[i][j - 1] < 9:
            nextPoint.append((i, j - 1))
        if i + 1 < len(grid) and (i + 1, j) not in visited and (i + 1, j) not in nextPoint and grid[i + 1][j] < 9:
            nextPoint.append((i + 1, j))
        if j + 1 < len(grid[i]) and (i, j + 1) not in visited and (i, j + 1) not in nextPoint and grid[i][j + 1] < 9:
            nextPoint.append((i, j + 1))
    basins.append(len(visited))
print(lowPoints)
basins.sort()
print(functools.reduce(operator.mul, basins[-3:]))