import heapq

file = open('input.txt')

grid = []
for line in file:
    grid.append([int(val) for val in line.strip()])

for row in grid:
    for i in range(4 * len(row)):
        if row[i%len(row)] + i // len(row) + 1 > 9:
            row.append(row[i%len(row)] + i // len(row) - 8)
        else:
            row.append(row[i%len(row)] + i // len(row) + 1)
for j in range(len(grid) * 4):
    nextRow = []
    row = grid[j % len(grid)]
    for i in range(len(row)):
        if row[i] + j // len(grid) + 1 > 9:
            nextRow.append(row[i] + j // len(grid) - 8)
        else:
            nextRow.append(row[i] + j // len(grid) + 1)
    grid.append(nextRow)

end = (len(grid[0]) - 1, len(grid) - 1)
heap = []
heapq.heappush(heap, (0, (0,0)))
previous = dict()
dists = dict()
previous[(0,0)] = None
dists[(0,0)] = 0
score, curr = heapq.heappop(heap)
while curr != end:
    nexts = []
    x, y = curr
    if x > 0 and (x-1, y):
        nexts.append((x-1, y))
    if y > 0 and (x, y-1):
        nexts.append((x, y-1))
    if x < len(grid[0]) - 1:
        nexts.append((x+1, y))
    if y < len(grid) - 1:
        nexts.append((x, y+1))
    for next in nexts:
        if next not in dists or score + grid[y][x] < dists[next]:
            heapq.heappush(heap, (score + grid[y][x], next))
            previous[next] = curr
            dists[next] = score + grid[y][x]
    score, curr = heapq.heappop(heap)

newScore = 0
while curr != (0,0):
    newScore += grid[curr[1]][curr[0]]
    curr = previous[curr]
print(score, curr, newScore)