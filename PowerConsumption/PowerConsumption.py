file = open("input.txt")


def search_space(inputs, pos, oxymode):
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
        most_common = 1
    else:
        most_common = 0

    subset = []
    for inp in inputs:
        if oxymode and inp[pos] == most_common:
            subset.append(inp)
        elif not oxymode and inp[pos] != most_common:
            subset.append(inp)

    return search_space(subset, pos + 1, oxymode)


def convert(bits):
    res = 0
    for bit in bits:
        res = (res << 1) | bit
    return res


inputs = []
for line in file:
    inputs.append([int(val) for val in list(line.strip())])

print(convert(search_space(inputs, 0, True)) * convert(search_space(inputs, 0, False)))