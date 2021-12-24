file = open('input.txt')


def func(params, z, w):
    if (z % 26) + params[1] != w:
        return z // params[0] * 26 + w + params[2]
    else:
        return z // params[0]


program = []
params = []
for line in file:
    program.append(line.strip().split())

for i in range(0, 18 * 14, 18):
    param1 = int(program[i + 4][-1])
    param2 = int(program[i + 5][-1])
    param3 = int(program[i + 15][-1])
    params.append((param1, param2, param3))

zs = {0: [0, 0]}
for param in params:
    newZs = {}
    for z, inp in zs.items():
        for i in range(1, 10):
            newZ = func(param, z, i)
            if param[0] == 1 or (param[0] == 26 and newZ < z):
                if newZ not in newZs:
                    newZs[newZ] = [inp[0] * 10 + i, inp[1] * 10 + i]
                else:
                    newZs[newZ][0] = min(newZs[newZ][0], inp[0] * 10 + i)
                    newZs[newZ][1] = max(newZs[newZ][1], inp[1] * 10 + i)
    print(len(newZs))
    zs = newZs
print(zs[0])