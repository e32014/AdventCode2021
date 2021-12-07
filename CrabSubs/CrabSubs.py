import math

file = open("input.txt")

pos = [int(val) for val in file.readline().strip().split(",")]

minDistance = math.inf
best_guess = None
for guess in range(min(pos), max(pos) + 1):
    distance = 0
    for i in pos:
        distance = distance + math.comb(abs(guess - i) + 1, 2)
    if distance < minDistance:
        minDistance = distance
        best_guess = guess

print(minDistance)
print(best_guess)