file = open('input.txt')

eastward = set()
southward = set()
ypos = 0
xpos = 0
for line in file:
    xpos = 0
    for char in line.strip():
        if char == '>':
            eastward.add((xpos, ypos))
        elif char == 'v':
            southward.add((xpos, ypos))
        xpos += 1
    ypos += 1
width = xpos
height = ypos

count = 0
while True:
    newEasts = set()
    newSouths = set()
    for x, y in eastward:
        if ((x + 1) % width, y) not in eastward and ((x + 1) % width, y) not in southward:
            newEasts.add(((x + 1) % width, y))
        else:
            newEasts.add((x, y))
    for x, y in southward:
        if (x, (y + 1) % height) not in newEasts and (x, (y + 1) % height) not in southward:
            newSouths.add((x, (y + 1) % height))
        else:
            newSouths.add((x, y))
    count += 1
    if newEasts == eastward and newSouths == southward:
        print(count)
        break
    eastward = newEasts
    southward = newSouths