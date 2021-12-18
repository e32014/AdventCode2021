import copy
import math
import re
from math import floor, ceil

file = open('input.txt')

class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
        self.parent = None

def interpParen(tokens, pos):
    if tokens[pos] == "[":
        pair = Tree()
        left, newpos = interpParen(tokens, pos + 1)
        right, newpos = interpParen(tokens, newpos)
        pair.left = left
        pair.right = right
        right.parent = pair
        left.parent = pair
        return pair, newpos + 1
    else:
        val = Tree()
        val.data = int(tokens[pos])
        return val, pos + 1


def explode(snailNum, depth):
    if depth >= 4 and snailNum.data is None:
        if snailNum.parent.left == snailNum:
            parent = snailNum.parent
            while parent.parent is not None and parent.parent.right != parent:
                parent = parent.parent
            parent = parent.parent
            if parent is not None:
                neighbor = parent.left
                while neighbor.data is None:
                    neighbor = neighbor.right
                neighbor.data += snailNum.left.data
            right = snailNum.parent.right
            while right.data is None:
                right = right.left
            right.data += snailNum.right.data
        else:
            parent = snailNum.parent
            while parent.parent is not None and parent.parent.left != parent:
                parent = parent.parent
            parent = parent.parent
            if parent is not None:
                neighbor = parent.right
                while neighbor.data is None:
                    neighbor = neighbor.left
                neighbor.data += snailNum.right.data
            left = snailNum.parent.left
            while left.data is None:
                left = left.right
            left.data += snailNum.left.data

        snailNum.data = 0
        snailNum.left = None
        snailNum.right = None
        return True
    elif snailNum.data is not None:
        return False
    else:
        return explode(snailNum.left, depth + 1) or explode(snailNum.right, depth + 1)

def split(snailNum):
    if snailNum.data is not None:
        if snailNum.data > 9:
            left = Tree()
            left.parent = snailNum
            left.data = floor(snailNum.data / 2.0)
            right = Tree()
            right.parent = snailNum
            right.data = ceil(snailNum.data / 2.0)
            snailNum.data = None
            snailNum.left = left
            snailNum.right = right
            return True
        else:
            return False
    else:
        return split(snailNum.left) or split(snailNum.right)


def printTree(tree):
    if tree.data is not None:
        return str(tree.data)
    else:
        return "[" + printTree(tree.left) + ", " + printTree(tree.right) + "]"


def calcTree(tree):
    if tree.data is not None:
        return tree.data
    else:
        return 3 * calcTree(tree.left) + 2 * calcTree(tree.right)


snailNums = []
for line in file:
    tokens = re.findall("\[|]|\d+",line.strip())
    parsed, _ = interpParen(tokens, 0)
    snailNums.append(parsed)

maxVal = -math.inf
for i in range(0, len(snailNums)):
    for j in range(0, len(snailNums)):
        if i == j:
            continue
        base = Tree()
        base.left = copy.deepcopy(snailNums[i])
        base.right = copy.deepcopy(snailNums[j])
        base.left.parent = base
        base.right.parent = base
        hasSplit = True
        while hasSplit:
            while explode(base, 0):
                continue
            hasSplit = split(base)
        val = calcTree(base)
        if val > maxVal:
            maxVal = val
print(maxVal)