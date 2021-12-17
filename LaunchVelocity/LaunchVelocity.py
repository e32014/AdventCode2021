import math
import re

file = open('input.txt')

xmin, xmax, ymin, ymax = [ int(val) for val in re.match('target area: x=(-?[0-9]+)..(-?[0-9]+), y=(-?[0-9]+)..(-?[0-9]+)', file.readline().strip()).groups()]

def simulate(startVelo, xmin, xmax, ymin, ymax):
    pos = (0, 0)
    velo = startVelo
    while pos[1] >= ymin and pos[0] <= xmax:
        x, y = pos
        velx, vely = velo
        pos = (x + velx, y + vely)
        if velx > 0:
            velx = velx - 1
        elif velx < 0:
            velx = velx + 1
        velo = (velx, vely - 1)
        if xmin <= x <= xmax and ymin <= y <= ymax:
            return True
    return False

landingVelos = []
print(xmin, xmax, ymin, ymax)
for x in range(0, xmax + 1):
    for y in range(ymin, abs(ymin) + 1):
        if simulate((x,y), xmin, xmax, ymin, ymax):
            landingVelos.append((x, y))

print(len(landingVelos))