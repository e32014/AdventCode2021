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
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] > 9:
                    flashes += 1
                    matrix[i][j] = 0
                    if i - 1 >= 0 and j - 1 >= 0 and matrix[i-1][j-1] != 0:
                        matrix[i-1][j-1] = min(matrix[i-1][j-1] + 1, 10)
                    if i - 1 >= 0 and matrix[i-1][j] != 0:
                        matrix[i-1][j] = min(matrix[i-1][j] + 1, 10)
                    if i - 1 >= 0 and j + 1 < len(matrix[j]) and matrix[i-1][j+1] != 0:
                        matrix[i-1][j+1] = min(matrix[i-1][j + 1] + 1, 10)
                    if j - 1 >= 0 and matrix[i][j-1] != 0:
                        matrix[i][j-1] = min(matrix[i][j-1] + 1, 10)
                    if j + 1 < len(matrix[i]) and matrix[i][j+1] != 0:
                        matrix[i][j+1] = min(matrix[i][j+1] + 1, 10)
                    if i + 1 < len(matrix) and j - 1 >= 0 and matrix[i+1][j-1] != 0:
                        matrix[i+1][j-1] = min(matrix[i+1][j-1] + 1, 10)
                    if i + 1 < len(matrix) and matrix[i+1][j] != 0:
                        matrix[i+1][j] = min(matrix[i+1][j] + 1, 10)
                    if i + 1 < len(matrix) and j + 1 < len(matrix[i]) and matrix[i+1][j+1] != 0:
                        matrix[i+1][j+1] = min(matrix[i+1][j + 1] + 1, 10)
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