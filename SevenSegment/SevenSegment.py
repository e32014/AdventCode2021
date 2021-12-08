file = open("input.txt")

inputs = []
outputs = []
display = {0: [1, 1, 1, 0, 1, 1, 1],
           1: [0, 0, 1, 0, 0, 1, 0],
           2: [1, 0, 1, 1, 1, 0, 1],
           3: [1, 0, 1, 1, 0, 1, 1],
           4: [0, 1, 1, 1, 0, 1, 0],
           5: [1, 1, 0, 1, 0, 1, 1],
           6: [1, 1, 0, 1, 1, 1, 1],
           7: [1, 0, 1, 0, 0, 1, 0],
           8: [1, 1, 1, 1, 1, 1, 1],
           9: [1, 1, 1, 1, 0, 1, 1]}
total = 0
for line in file:
    inputs = line.strip().split("|")[0].strip().split()
    outputs = line.strip().split("|")[1].strip().split()
    mapping = dict()
    for i in range(7):
        mapping[i] = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}

    lens = dict()
    for inp in inputs:
        lens[len(inp)] = lens.setdefault(len(inp), list()) + [inp]

    for i in range(7):
        if display[1][i] == 1:
            mapping[i] = set(lens[2][0]).intersection(mapping.get(i))
        else:
            mapping[i] = mapping[i] - set(lens[2][0])

    for i in range(7):
        if display[4][i] == 1:
            mapping[i] = set(lens[4][0]).intersection(mapping.get(i))
        else:
            mapping[i] = mapping[i] - set(lens[4][0])

    for i in range(7):
        if display[7][i] == 1:
            mapping[i] = set(lens[3][0]).intersection(mapping.get(i))
        else:
            mapping[i] = mapping[i] - set(lens[3][0])
    original = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    inEach = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    missing = {}
    for val in lens[6]:
        inEach = inEach.intersection(set(val))
    missing = original - inEach
    for i in range(7):
        if i == 2 or i == 3 or i == 4:
            mapping[i] = missing.intersection(mapping.get(i))
        else:
            mapping[i] = mapping[i] - missing

    inv_mapping = dict()
    for key, val in mapping.items():
        inv_mapping[val.pop()] = key

    value = 0
    for output in outputs:
        disp = [0] * 7
        for char in output:
            disp[inv_mapping[char]] = 1
        for key, val in display.items():
            if val == disp:
                value = value * 10 + key
    total += value
print(total)