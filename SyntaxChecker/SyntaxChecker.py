from statistics import median

file = open("input.txt")

score = 0
matches = {"{": "}", "[":"]", "<": ">", "(": ")"}
scores = {"}": 1197, "]": 57, ">": 25137, ")": 3}
autoScores = {")": 1, "]": 2, "}":3, ">": 4}
autoList = []
for line in file:
    command = line.strip()
    stack = []
    curr = ""
    err = ""
    for char in command:
        if char in matches:
            stack.append(curr)
            curr = char
        elif curr == "" and char not in matches:
            err = char
            break
        elif curr != "" and char not in matches and matches[curr] == char:
            curr = stack.pop()
        elif curr != "" and char not in matches and matches[curr] != char:
            err = char
            break

    if err != "":
        score += scores[err]
        continue
    stack.append(curr)
    autoScore = 0
    for i in range(len(stack)-1, 0, -1):
        autoScore = autoScore * 5 + autoScores[matches[stack[i]]]
    autoList.append(autoScore)

print(score)
print(median(autoList))