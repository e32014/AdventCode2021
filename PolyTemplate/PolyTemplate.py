import re
from collections import Counter

def countAll(pair, counter, rules, iters):
    if iters == 0:
        counter


file = open("input.txt")

polymer = file.readline().strip()
file.readline()

rules = dict()
rule = file.readline().strip()
while rule != "":
    pair, sub = re.match("([A-Za-z]+) -> ([A-Za-z])", rule).groups()
    rules[pair] = sub
    rule = file.readline().strip()

iterations = 40
count = Counter()
for i in range(len(polymer) - 1):
    count[polymer[i:i+2]] += 1
for _ in range(iterations):
    newCount = Counter()
    for pair in count:
        if pair in rules:
            char = rules[pair]
            newCount[pair[0] + char] += count[pair]
            newCount[char + pair[1]] += count[pair]
        else:
            newCount[pair] += count[pair]
    count = newCount
charCount = Counter()
for pair in count.keys():
    charCount[pair[0]] += count[pair]
    charCount[pair[1]] += count[pair]
for char in polymer:
    charCount[char] += 1
for key in charCount.keys():
    charCount[key] = charCount[key] // 2
print(charCount)
print(charCount.most_common()[0][1] - charCount.most_common()[-1][1])