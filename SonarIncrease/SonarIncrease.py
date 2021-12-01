
input = open("input.txt")

count = 0
curr = [None, None, None]
prev = [None, None, None]
for line in input:
    val = int(line.strip())
    curr = curr[1:] + [val]
    if None not in prev and sum(prev) < sum(curr):
        count += 1
    prev = curr

print(count)