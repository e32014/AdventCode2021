import re
from collections import Counter


def volume(x, y, z):
   return (x[1] - x[0] + 1) * (y[1] - y[0] + 1) * (z[1] - z[0] + 1)


file = open('input.txt')

dirs = []
for line in file:
    mode, xmin, xmax, ymin, ymax, zmin, zmax = re.match("(on|off) x=(-?[0-9]+)..(-?[0-9]+),y=(-?[0-9]+)..(-?[0-9]+),z=(-?[0-9]+)..(-?[0-9]+)", line.strip()).groups()
    dirs.append((mode, int(xmin), int(xmax), int(ymin), int(ymax), int(zmin), int(zmax)))

cubes = Counter()
for dir in dirs:
    mode1, xmin, xmax, ymin, ymax, zmin, zmax = dir
    consideredUpdate = Counter()
    for (x1min, x1max, y1min, y1max, z1min, z1max), nmode in cubes.items():
        subXmin = max(xmin, x1min)
        subXmax= min(xmax, x1max)
        subYmin = max(ymin, y1min)
        subYmax = min(ymax, y1max)
        subZmin = max(zmin, z1min)
        subZmax =  min(zmax, z1max)
        if subXmin <=  subXmax and subYmin <= subYmax and subZmin <= subZmax:
            consideredUpdate[(subXmin, subXmax, subYmin, subYmax, subZmin, subZmax)] -= nmode
    if mode1 == 'on':
        consideredUpdate[(xmin, xmax, ymin, ymax, zmin, zmax)] += 1
    cubes.update(consideredUpdate)

total = 0
for (xmin, xmax, ymin, ymax, zmin, zmax), sign in cubes.items():
    total += sign * volume((xmin, xmax), (ymin, ymax), (zmin, zmax))
print(total)