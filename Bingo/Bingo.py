file = open("input.txt")

calls = [int(x) for x in file.readline().strip().split(",")]

boards = []
currBoard = []
file.readline()
for line in file:
    if line.strip() == "":
        boards.append(currBoard)
        currBoard = []
        continue
    row = [int(x) for x in line.strip().split()]
    currBoard.append(row)
boards.append(currBoard)

lastBoard = None
winVal = None
removeBoards = []
for val in calls:
    for board in boards:
        for row in board:
            if val in row:
                row[row.index(val)] = 'X'
                break

        rowWin = False
        for i in range(len(board)):
            if board[i].count('X') == len(board[i]):
                rowWin = True
                break

        colWin = False
        for i in range(len(board)):
            col = []
            for j in range(len(board[i])):
                col.append(board[j][i])
            if col.count('X') == len(col):
                colWin = True
                break

        if colWin or rowWin:
            lastBoard = board
            winVal = val
            removeBoards.append(board)
    if len(removeBoards) > 0:
        for board in removeBoards:
            boards.remove(board)
        removeBoards = []
    if len(boards) == 0:
        break

total = 0
for row in lastBoard:
    total += sum([val for val in row if val != 'X'])
print(total * winVal)
print(lastBoard)