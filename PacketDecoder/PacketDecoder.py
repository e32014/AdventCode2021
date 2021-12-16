from functools import reduce
from operator import mul

file = open("input.txt")

hexString = file.readline().strip()
binString = bin(int(hexString, 16))[2:].zfill(len(hexString) * 4)

def evalResults(code, vals):
    if code == 0:
        return sum(vals)
    elif code == 1:
        return reduce(mul, vals, 1)
    elif code == 2:
        return min(vals)
    elif code == 3:
        return max(vals)
    elif code == 5:
        return 1 if vals[0] > vals[1] else 0
    elif code == 6:
        return 1 if vals[0] < vals[1] else 0
    elif code == 7:
        return 1 if vals[0] == vals[1] else 0


def decodeData(packet, pos):
    version = int(packet[pos:pos + 3], 2)
    pos = pos + 3
    type = int(packet[pos:pos+3], 2)
    pos = pos + 3
    if type == 4:
        total = 0
        cont = int(packet[pos], 2)
        pos += 1
        val = int(packet[pos:pos+4], 2)
        pos += 4
        while cont == 1:
            total = (total << 4) + val
            cont = int(packet[pos], 2)
            pos += 1
            val = int(packet[pos:pos+4], 2)
            pos += 4
        total = (total << 4) + val
        return total, pos
    else:
        lenType = int(packet[pos], 2)
        pos += 1
        if lenType == 0:
            readSize = 0
            maxSize = int(packet[pos: pos + 15], 2)
            pos += 15
            subresults = []
            while readSize < maxSize:
                subresult, newPos = decodeData(packet, pos)
                readSize += newPos - pos
                subresults.append(subresult)
                pos = newPos
            return evalResults(type, subresults), pos
        else:
            subCount = int(packet[pos: pos + 11], 2)
            pos += 11
            subresults = []
            for _ in range(subCount):
                subresult, newPos = decodeData(packet, pos)
                subresults.append(subresult)
                pos = newPos
            return evalResults(type, subresults), pos


result, _ = decodeData(binString, 0)
print(result)