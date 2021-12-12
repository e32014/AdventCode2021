from copy import deepcopy

file = open('input.txt')


def checkAllPaths(graph, curr, visited, paths, upToNow):
    if curr == 'end':
        paths.append(upToNow + [curr])
        return

    nextVisit = deepcopy(visited)
    if curr.islower():
        nextVisit[curr] = nextVisit.setdefault(curr, 0) + 1
    for next in graph[curr]:
        if (next == 'start' or next == 'end') and next in visited and visited[next] == 1:
            continue
        if next in visited and visited[next] > 0 and any(val == 2 for val in nextVisit.values()):
            continue
        if next not in visited or visited[next] < 2:
            checkAllPaths(graph, next, nextVisit, paths, upToNow + [curr])

graph = dict()
for line in file:
    edge = line.strip().split("-")
    graph.setdefault(edge[0], []).append(edge[1])
    graph.setdefault(edge[1], []).append(edge[0])

print(graph)

paths = []
checkAllPaths(graph, 'start', dict(), paths, [])
print(len(paths))