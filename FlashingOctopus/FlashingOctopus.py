from copy import deepcopy

file = open('input.txt')

matrix = []
for line in file:
    matrix.append([int(val) for val in line.strip()])

iterations = 0
flashes = 0
while True:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = min(matrix[i][j] + 1, 10)

    while any(10 in row for row in matrix):
        newMatrix = deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] > 9:
                    flashes += 1
                    newMatrix[i][j] = 0
                    if i - 1 >= 0 and j - 1 >= 0 and newMatrix[i-1][j-1] != 0:
                        newMatrix[i-1][j-1] = min(newMatrix[i-1][j-1] + 1, 10)
                    if i - 1 >= 0 and newMatrix[i-1][j] != 0:
                        newMatrix[i-1][j] = min(newMatrix[i-1][j] + 1, 10)
                    if i - 1 >= 0 and j + 1 < len(newMatrix[j]) and newMatrix[i-1][j+1] != 0:
                        newMatrix[i-1][j+1] = min(newMatrix[i-1][j + 1] + 1, 10)
                    if j - 1 >= 0 and newMatrix[i][j-1] != 0:
                        newMatrix[i][j-1] = min(newMatrix[i][j-1] + 1, 10)
                    if j + 1 < len(newMatrix[i]) and newMatrix[i][j+1] != 0:
                        newMatrix[i][j+1] = min(newMatrix[i][j+1] + 1, 10)
                    if i + 1 < len(newMatrix) and j - 1 >= 0 and newMatrix[i+1][j-1] != 0:
                        newMatrix[i+1][j-1] = min(newMatrix[i+1][j-1] + 1, 10)
                    if i + 1 < len(newMatrix) and newMatrix[i+1][j] != 0:
                        newMatrix[i+1][j] = min(newMatrix[i+1][j] + 1, 10)
                    if i + 1 < len(newMatrix) and j + 1 < len(newMatrix[i]) and newMatrix[i+1][j+1] != 0:
                        newMatrix[i+1][j+1] = min(newMatrix[i+1][j + 1] + 1, 10)
        matrix = newMatrix
    allFlash = True
    for row in matrix:
        for val in row:
            if val != 0:
                allFlash = False
                break
        if not allFlash:
            break
    if allFlash:
        print(iterations + 1)
        break
    iterations += 1
print(matrix)
print(flashes)