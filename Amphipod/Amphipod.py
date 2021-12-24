import copy
import heapq
board = []
maxStack = 4
def isFinished(board, expected):
    for line in range(len(board)):
        if line == 1:
            for char in range(1, len(board[line]) - 1):
                if board[line][char] != '.':
                    return False
        elif 1 < line <= maxStack + 1:
            for char in range(0, len(board[line])):
                if board[line][char] in expected and expected[board[line][char]] != char:
                    return False
    return True

def genBoard(stacks, hall, emptyBoard, changes=None):
    if changes is None:
        changes = dict()
    newBoard = []
    for line in range(len(emptyBoard)):
        if line == 1:
            newHall = ""
            for char in range(len(emptyBoard[line])):
                if (line, char) in changes:
                    newHall += changes[(line, char)]
                elif (line, char) in hall:
                    newHall += hall[(line, char)]
                else:
                    newHall += emptyBoard[line][char]
            newBoard.append(newHall)
        elif 1 < line <= maxStack + 1:
            newLine = ""
            for char in range(len(emptyBoard[line])):
                if (line, char) in changes:
                    newLine += changes[(line, char)]
                elif char in stacks:
                    if len(stacks[char]) > (maxStack - line + 1):
                        newLine += stacks[char][maxStack - line + 1]
                    else:
                        newLine += '.'
                else:
                    newLine += emptyBoard[line][char]
            newBoard.append(newLine)
        else:
            newBoard.append(emptyBoard[line])
    return newBoard


for line in open('input.txt'):
    board.append(line.strip("\n"))

emptyBoard = []
validHalls = []
for i in range(len(board)):
    emptyline = ""
    for j in range(len(board[i])):
        if i == 1 and board[i+1][j] == '#' and board[i][j] == '.':
            validHalls.append((i, j))
        if not (board[i][j] == '#' or board[i][j] == '.' or board[i][j] == ' '):
            emptyline += '.'
        else:
            emptyline += board[i][j]
    emptyBoard.append(emptyline)
print(validHalls)
expected = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
prev = dict()
queue = []
visited = set()
prev[''.join(board)] = (0, None)
heapq.heappush(queue, (0, board))
while len(queue) > 0:
    score, board = heapq.heappop(queue)
    visited.add(''.join(board))
    print(score, board)
    if isFinished(board, expected):
        print(score)
        break
    stacks = dict()
    for line in range(len(board) - 1, 1, -1):
        for char in range(len(board[line])):
            if board[line][char] != '#' and board[line][char] != ' ':
                if board[line][char] != '.':
                    stacks.setdefault(char, []).append(board[line][char])
                elif char not in stacks:
                    stacks[char] = []
    hall = dict()
    for char in range(len(board[1])):
        if board[1][char] != '#' and board[1][char] != ' ' and board[1][char] != '.':
            hall[(1, char)] = board[1][char]

    for (y, x), char in hall.items():
        blocked = False
        for pos in range(min(expected[char], x), max(expected[char], x) + 1):
            if (y, pos) in hall and x != pos:
                blocked = True
        if len(stacks[expected[char]]) < maxStack and not blocked:
            allmatch = True
            for chr in stacks[expected[char]]:
                if chr != char:
                    allmatch = False
            if not allmatch:
                continue
            newBoard = genBoard(stacks, hall, emptyBoard, {(y, x): '.', ((maxStack - len(stacks[expected[char]]) + 1), expected[char]): char})
            newScore = score + (abs(expected.get(char) - x) + abs(maxStack + 1 - len(stacks[expected[char]]) - y)) * costs.get(char)
            print(newBoard, newScore)
            if ''.join(newBoard) not in visited or prev[''.join(newBoard)][0] > score + newScore:
                prev[''.join(newBoard)] = (newScore, board)
                heapq.heappush(queue, (newScore, newBoard))

    for x, chars in stacks.items():
        if len(chars) == 0:
            continue
        for (hally, hallx) in validHalls:
            blocked = False
            for pos in range(min(hallx, x), max(hallx, x) + 1):
                if(hally, pos) in hall:
                    blocked = True
            if not blocked:
                newBoard = genBoard(stacks, hall, emptyBoard, {(hally, hallx): chars[-1], (maxStack + 2 - len(chars), x): '.'})
                newScore = score + (abs(hallx - x) + abs(hally - (maxStack + 2 - len(chars)))) * costs.get(chars[-1])
                print(newBoard, newScore)
                if ''.join(newBoard) not in prev or prev[''.join(newBoard)][0] > newScore:
                    prev[''.join(newBoard)] = (newScore, board)
                    heapq.heappush(queue, (newScore, newBoard))