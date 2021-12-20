file = open("input.txt")

def displayGrid(grid):
    maxX = max([x for x, _ in grid]) + 1
    maxY = max([y for _, y in grid]) + 1
    minX = min([x for x, _ in grid])
    minY = min([y for _, y in grid])
    dispGrid = [["."] * (maxX - minX) for _ in range(minY, maxY)]

    for x, y in grid:
        dispGrid[y - minY][x - minX] = '#'
    for row in dispGrid:
        print("".join(row))


algo = file.readline().strip()
alternates = algo[0] == '#' and algo[-1] == '.'
file.readline()
ypos = 0
grid = set()
for line in file:
    xpos = 0
    for char in line.strip():
        if char == '#':
            grid.add((xpos, ypos))
        xpos += 1
    ypos += 1

iterations = 50
for step in range(iterations):
    newGrid = set()
    displayGrid(grid)
    print("--------------------")
    maxX = max([x for x, _ in grid]) + 1
    maxY = max([y for _, y in grid]) + 1
    minX = min([x for x, _ in grid])
    minY = min([y for _, y in grid])
    for y in range(minY - 3, maxY + 3):
        for x in range(minX - 3, maxX + 3):
            num = []
            for offy in [y -1, y, y+1]:
                for offx in [x - 1, x, x + 1]:
                    if minX <= offx < maxX and minY <= offy < maxY:
                        if (offx, offy) in grid:
                            num.append("1")
                        else:
                            num.append("0")
                    elif alternates:
                        num.append(str(step%2))
            if algo[int("".join(num),2)] == '#':
                newGrid.add((x, y))
    grid = newGrid
displayGrid(grid)
print(len(grid))