import math
from copy import deepcopy

file = open('input.txt')

def checkOverlap(scan1, scan2, start1, start2):
    matches = 0
    relatives1 = set()
    relatives2 = set()
    for beacon in scan1:
        relatives1.add((beacon[0] - start1[0], beacon[1] - start1[1], beacon[2] - start1[2]))
    for beacon2 in scan2:
        relatives2.add((beacon2[0] - start2[0], beacon2[1] - start2[1], beacon2[2] - start2[2]))
    for relative in relatives1:
        if relative in relatives2:
            matches += 1
    return matches

def allUps(scans):
    ups = [scans]
    upsidedown = []
    oneturn = []
    threeturn = []
    for scan in scans:
        oneturn.append([scan[0], scan[2], -1*scan[1]])
        upsidedown.append([scan[0], -1 * scan[1], -1 * scan[2]])
        threeturn.append([scan[0], -1*scan[2], scan[1]])
    ups.append(oneturn)
    ups.append(upsidedown)
    ups.append(threeturn)
    return ups


def allRotations(scans):
    rotations = allUps(scans)
    oppX = []
    for scan in scans:
        oppX.append([-1*scan[0], scan[1], -1*scan[2]])
    rotations += allUps(oppX)
    dirY = []
    oppY = []
    for scan in scans:
        dirY.append([scan[1], -1*scan[0], scan[2]])
        oppY.append([-1 * scan[1], scan[0], scan[2]])
    rotations += allUps(dirY)
    rotations += allUps(oppY)
    dirZ = []
    oppZ = []
    for scan in scans:
        dirZ.append([scan[2], scan[1], -1 * scan[0]])
        oppZ.append([-1 * scan[2], scan[1], scan[0]])
    rotations += allUps(dirZ)
    rotations += allUps(oppZ)
    return rotations


scans = []
beacons = []
for line in file:
    if line.strip().startswith("---"):
        if len(beacons) > 0:
            scans.append(beacons)
            beacons = []
    elif line.strip() != '':
        beacons.append(list(map(int, line.strip().split(","))))
scans.append(beacons)

poses = {0: ((0, 0, 0), scans[0])}
rotated = dict()
for i in range(1, len(scans)):
    rotated[i] = allRotations(scans[i])
lockedIn = [0]
while len(poses) < len(scans):
    newPoses = dict()
    key = lockedIn.pop()

    pos, orientedScan = poses[key]
    for j in range(len(scans)):
        if j in newPoses or j in poses:
            continue
        rots = rotated[j]
        for m in range(len(orientedScan)):
            for r in range(len(rots)):
                for k in range(len(scans[j])):
                    count = checkOverlap(orientedScan, rots[r], orientedScan[m], rots[r][k])
                    if count >= 12:
                        print(str(orientedScan[m]) + " = " + str(rots[r][k]) + ", " + str(scans[j][k]) + ", " + str(key) + ", " + str(len(poses)))
                        newPoses[j] = ((orientedScan[m][0] - rots[r][k][0] + pos[0], orientedScan[m][1] - rots[r][k][1] + pos[1], orientedScan[m][2] - rots[r][k][2] + pos[2]), rots[r])
                        lockedIn.append(j)
                        break
                if j in newPoses:
                    break
            if j in newPoses:
                break

    poses.update(newPoses)

beaconSet = set()
for i in range(len(scans)):
    pos, rotation = poses[i]
    for beacon in rotation:
        beaconSet.add((beacon[0] + pos[0], beacon[1] + pos[1], beacon[2] + pos[2]))
print(len(beaconSet))

maxMan = -math.inf
for i in range(len(scans)):
    for j in range(len(scans)):
        if i == j:
            continue
        pos1, _ = poses[i]
        pos2, _ = poses[j]
        manDist = sum([abs(pos1[k] - pos2[k]) for k in range(3)])
        if manDist > maxMan:
            maxMan = manDist
print(maxMan)