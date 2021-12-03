file = open("input.txt")

def searchSpace(inputs, pos, oxymode):
    if len(inputs) == 1:
        return inputs[0]
    ones = 0
    zeros = 0
    for inp in inputs:
        if inp[pos] == 0:
            zeros += 1
        else:
            ones += 1

    if ones >= zeros:
        mostCommon = 1
    else:
        mostCommon = 0

    subset = []
    for inp in inputs:
        if oxymode and inp[pos] == mostCommon:
            subset.append(inp)
        elif not oxymode and inp[pos] != mostCommon:
            subset.append(inp)

    return searchSpace(subset, pos + 1, oxymode)

def convert(bits):
    res = 0
    for bit in bits:
        res = (res << 1) | bit
    return res

inputs = []
for line in file:
    inputs.append([int(val) for val in list(line.strip())])

print(convert(searchSpace(inputs, 0, True)) * convert(searchSpace(inputs, 0, False)))