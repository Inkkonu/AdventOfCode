from collections import defaultdict
from math import floor


def p1(data):
    total = 0
    rules = data[0]
    for line in data[1]:
        total += line[floor(len(line)/2)] if isCorrect(rules, line) else 0
    return total


def p2(data):
    total = 0
    rules = data[0]
    for line in data[1]:
        if not isCorrect(rules, line):
            newLine = []
            for v in line:
                newLine.append(v)
                i = len(newLine) - 1
                while not isCorrect(rules, newLine):
                    newLine[i], newLine[i-1] = newLine[i-1], newLine[i]
                    i -= 1
            total += newLine[floor(len(newLine)/2)
                             ] if isCorrect(rules, newLine) else 0
    return total


def isCorrect(rules, line):
    correct = True
    for i, v in enumerate(line):
        afters = rules[v]
        for after in afters:
            if after in line and line.index(after) < i:
                correct = False
    return correct


if __name__ == '__main__':
    rules = defaultdict(list)
    data = [rules, []]
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if line != "":
                if "|" in line:
                    line = line.split("|")
                    before, after = int(line[0]), int(line[1])
                    rules[before].append(after)
                else:
                    line = list(map(int, line.split(",")))
                    data[1].append(line)
    print(f'Part 1 : {p1(data)}')
    print(f'Part 2 : {p2(data)}')
